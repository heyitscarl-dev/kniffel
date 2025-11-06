use std::time::SystemTime;

use jsonwebtoken::{DecodingKey, EncodingKey, Header, Validation, decode, encode};

use crate::auth::{claims::Claims, error::Result};

#[derive(Clone)]
pub struct Keys {
    pub encoding: EncodingKey,
    pub decoding: DecodingKey,
}

impl Keys {
    pub fn new(secret: &str) -> Self {
        Keys {
            encoding: EncodingKey::from_secret(secret.as_bytes()),
            decoding: DecodingKey::from_secret(secret.as_bytes()),
        }
    }
}

pub fn encode_jwt(keys: &Keys, claims: &Claims) -> Result<String> {
    let token = encode(&Header::default(), claims, &keys.encoding)?;
    Ok(token)
}

pub fn decode_jwt(keys: &Keys, token: String) -> Result<Claims> {
    let data = decode::<Claims>(token, &keys.decoding, &Validation::default())?;
    Ok(data.claims)
}
