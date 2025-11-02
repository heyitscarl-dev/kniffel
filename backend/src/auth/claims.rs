use serde::{Deserialize, Serialize};

use crate::auth::{self, error::Error};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Claims {
    pub typ: TokenType,      // type (e.g. "session", or "match")
    pub sub: Option<String>, // subject
    pub iat: i64,            // issued at
    pub iss: String,         // issuer / issued by
    pub exp: i64,            // expire at
    pub jti: String,         // unique token
}

#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
pub enum TokenType {
    Session,
    Match,
}

impl TryFrom<String> for TokenType {
    type Error = auth::error::Error;

    fn try_from(value: String) -> Result<Self, Self::Error> {
        match value.as_str() {
            "session" => Ok(Self::Session),
            "match" => Ok(Self::Match),
            _ => Err(Error::InvalidType(value)),
        }
    }
}
