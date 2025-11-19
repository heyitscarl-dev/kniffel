use axum::response::IntoResponse;
use thiserror::Error;

use crate::auth::claims::ClaimsType;

#[derive(Debug, Error)]
pub enum AuthError {
    #[error(transparent)]
    JWTError(#[from] jsonwebtoken::errors::Error),

    #[error("Invalid Claims Type (typ): Expected {:?} but got {:?}.", 0, 1)]
    ClaimsType(ClaimsType, ClaimsType),

    #[error("Invalid Claims Subject (sub): {}", 0)]
    ClaimsSub(String),
}

pub type Result<T> = std::result::Result<T, AuthError>;

impl IntoResponse for AuthError {
    fn into_response(self) -> axum::response::Response {
        let status_code = match &self {
            AuthError::JWTError(_) => http::StatusCode::UNAUTHORIZED,
            AuthError::ClaimsType(_, _) => http::StatusCode::BAD_REQUEST,
            AuthError::ClaimsSub(_) => http::StatusCode::BAD_REQUEST,
        };

        let body = format!("Authentication error: {}", self);

        (status_code, body).into_response()
    }
}