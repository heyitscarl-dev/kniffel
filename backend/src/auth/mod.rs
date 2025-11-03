use std::sync::Arc;

use axum::{Json, extract::State, response::IntoResponse};
use chrono::{Duration, Utc};
use hyper::StatusCode;
use jsonwebtoken::{Algorithm, Header, Validation, decode, encode};
use serde::{Deserialize, Serialize};
use ulid::Ulid;
use uuid::Uuid;

use crate::{auth::claims::{Claims, TokenType}, AppState};

pub use error::{Error, Result};
pub use keys::Keys;

mod claims;
mod error;
mod keys;

#[derive(Debug, Serialize, Deserialize)]
pub struct Token(String);

impl Token {
    pub fn new(raw: impl Into<String>) -> Self {
        Self(raw.into())
    }

    pub fn raw<'a>(&'a self) -> &'a str {
        &self.0
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub(crate) struct RequestSessionParams {
    typ: String,
}

pub const EXP_HOURS: i64 = 24;
pub const ISS_IDENTIFIER: &'static str = "kniffel-backend";

pub async fn request_token(
    State((_, keys)): State<AppState>,
    Json(params): Json<RequestSessionParams>,
) -> Result<Json<Token>> {
    let typ: TokenType = params.typ.try_into()?;

    match typ {
        TokenType::Session => Ok(Json(issue_session(&keys, EXP_HOURS)?)),
        _ => unimplemented!("Match Tokens"),
    }
}

fn issue_session(keys: &Keys, hours: i64) -> Result<Token> {
    let iat = Utc::now().timestamp();
    let exp = (Utc::now() + Duration::hours(hours)).timestamp();

    let sub = Uuid::new_v4().to_string();

    let claims = Claims {
        typ: TokenType::Session,
        iss: String::from(ISS_IDENTIFIER),
        sub,
        iat,
        exp,
    };

    let header = Header::new(Algorithm::HS256);

    encode(&header, &claims, &keys.encode)
        .map_err(|err| Error::Serialization(err))
        .map(|ok| Token::new(ok))
}

pub fn verify_session(keys: &Keys, token: Token) -> Result<Claims> {
    let verified_at = Utc::now().timestamp();

    let token = decode::<Claims>(token.raw(), &keys.decode, &Validation::default())?;
    let claims = token.claims;

    if claims.exp < verified_at {
        return Err(Error::InvalidExpiry);
    }

    if claims.typ != TokenType::Session {
        return Err(Error::InvalidType(format!(
            "Expected {:?} but got {:?}",
            TokenType::Session,
            claims.typ
        )));
    }

    Ok(claims)
}
