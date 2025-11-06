use serde::{Deserialize, Serialize};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Claims {
    pub typ: ClaimsType,
    pub sub: String,
    pub iss: i64,
    pub exp: i64
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum ClaimsType {
    Session
}
