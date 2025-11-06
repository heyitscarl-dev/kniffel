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
pub type Fallible = Result<()>;
