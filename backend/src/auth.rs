use std::sync::Arc;

use axum::{extract::State, response::IntoResponse, Json};
use chrono::{Duration, Utc};
use hyper::StatusCode;
use jsonwebtoken::{decode, encode, Algorithm, DecodingKey, EncodingKey, Header, Validation};
use serde::{Deserialize, Serialize};
use thiserror::Error;

#[derive(Debug, Error, Serialize, Deserialize)]
pub enum AuthError {
    #[error("Wrong token type: Expected {} but got {}", 0, 1)]
    Mismatch(String, String),

    #[error("Expired token")]
    Expired,

    #[error(transparent)]
    #[serde(skip)]
    Other(#[from] jsonwebtoken::errors::Error)
}

impl IntoResponse for AuthError {
    fn into_response(self) -> axum::response::Response {
        (StatusCode::INTERNAL_SERVER_ERROR, self.to_string()).into_response()
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SessionClaims {
    pub typ: String,
    pub sub: String,
    pub iss: i64,
    pub exp: i64
}

#[derive(Debug, Clone)]
pub struct Keychain {
    encode: EncodingKey,
    decode: DecodingKey
}

impl Keychain {
    pub fn from_hs256(secret: &[u8]) -> Self {
        Self {
            encode: EncodingKey::from_secret(secret),
            decode: DecodingKey::from_secret(secret)
        }
    }
}

fn now() -> i64 { Utc::now().timestamp() }

pub async fn request_session(State(keychain): State<Arc<Keychain>>) -> Result<Json<String>, AuthError> {
    let token = issue_session(&keychain, 24)?;
    Ok(Json(token))
}

pub fn issue_session(keychain: &Keychain, duration_hours: i64) -> Result<String, AuthError> {
    let iss = now();
    let exp = (Utc::now() + Duration::hours(duration_hours)).timestamp();
    let claims = SessionClaims { typ: "session".to_string(), sub: String::from("Annonymous"), iss, exp };
    let header = Header::new(Algorithm::HS256);
    Ok(encode(&header, &claims, &keychain.encode)?)
}

pub fn verify_session(keychain: &Keychain, token: String) -> Result<SessionClaims, AuthError> {
    let mut validation = Validation::new(Algorithm::HS256);
    validation.validate_exp = true;
    let data = decode::<SessionClaims>(token, &keychain.decode, &validation)?;
    if data.claims.typ != "session" { return Err(AuthError::Mismatch("session".to_string(), data.claims.typ)) }
    if data.claims.exp <= now() { return Err(AuthError::Expired) }
    Ok(data.claims)
}
