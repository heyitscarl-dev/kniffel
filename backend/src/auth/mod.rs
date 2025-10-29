use std::sync::Arc;

use axum::{Json, extract::State, response::IntoResponse};
use chrono::{Duration, Utc};
use hyper::StatusCode;
use jsonwebtoken::{encode, Algorithm, Header};
use serde::{Deserialize, Serialize};
use ulid::Ulid;

use crate::auth::{
    claims::{Claims, TokenType},
    error::{Error, Result},
    keys::Keys,
};

mod claims;
mod error;
mod keys;

pub struct Token(String);

impl From<String> for Token {
    fn from(value: String) -> Self {
        Self(value)
    }
}

impl Into<String> for Token {
    fn into(self) -> String {
        self.0
    }
}

impl IntoResponse for Token {
    fn into_response(self) -> axum::response::Response {
        (StatusCode::OK, self.0).into_response()
    }
}

#[derive(Debug, Serialize, Deserialize)]
pub(crate) struct RequestSessionParams {
    typ: String,
}

pub const EXP_HOURS: i64 = 24;
pub const ISS_IDENTIFIER: &'static str = "kniffel-backend";

pub async fn request_token(
    State(keys): State<Arc<Keys>>,
    Json(params): Json<RequestSessionParams>,
) -> Result<Token> {
    let typ: TokenType = params.typ.try_into()?;

    match typ {
        TokenType::Session => issue_session(&keys, EXP_HOURS),
        _ => unimplemented!("Match Tokens")
    } 
}

fn issue_session(keys: &Keys, hours: i64) -> Result<Token> {
    let iat = Utc::now().timestamp();
    let exp = (Utc::now() + Duration::hours(hours)).timestamp();

    let jti = Ulid::new().to_string();

    let claims = Claims {
        sub: None,
        typ: TokenType::Session,
        iss: String::from(ISS_IDENTIFIER),
        iat,
        exp,
        jti,
    };

    let header = Header::new(Algorithm::HS256);

    encode(&header, &claims, &keys.encode)
        .map_err(|err| Error::Encoding(err))
        .map(|ok| ok.into())
}
