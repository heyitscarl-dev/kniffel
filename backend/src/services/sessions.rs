use std::sync::Arc;

use chrono::{Duration, Utc};
use serde::{Deserialize, Serialize};
use ulid::Ulid;

use crate::auth::{self, claims::{Claims, ClaimsType}, jwt::{self, Keys}};

#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct SessionID(String);

impl SessionID {
    pub fn new() -> Self {
        Self(Ulid::new().to_string())
    }

    pub fn ulid(&self) -> Ulid {
        Ulid::from_string(&self.0)
            .expect("Expected String contained in SessionID to be valid Ulid.")
    }

    pub fn try_from(string: &str) -> Option<Self> {
        Some(Self(
            Ulid::from_string(string)
                .ok()?
                .to_string()
        ))
    }
}

#[derive(Clone)]
pub struct SessionService {
    keys: Arc<Keys>,
    expire_after_hours: i64
}

impl SessionService {
    pub fn new(keys: Arc<Keys>, expire_after_hours: i64) -> Self {
        SessionService { keys, expire_after_hours }
    }

    pub fn issue_session(&self) -> auth::Result<String> {
        let session_id = SessionID::new();
        let claims = Claims { 
            typ: ClaimsType::Session, 
            sub: session_id.ulid().to_string(),
            iss: Utc::now().timestamp(),
            exp: (Utc::now() + Duration::hours(self.expire_after_hours)).timestamp()
        };
        jwt::encode_jwt(&self.keys, &claims)
    }

    pub fn validate_session(&self, token: String) -> auth::Result<SessionID> {
        let claims: Claims = jwt::decode_jwt(&self.keys, token)?;

        if ClaimsType::Session != claims.typ {
            return Err(auth::Error::ClaimsType(ClaimsType::Session, claims.typ));
        } else if let Some(session_id) = SessionID::try_from(&claims.sub) {
            return Ok(session_id)
        } else {
            return Err(auth::Error::ClaimsSub(claims.sub))
        }
    }
}
