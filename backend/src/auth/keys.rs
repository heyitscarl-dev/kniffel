use jsonwebtoken::{DecodingKey, EncodingKey};

pub struct Keys {
    pub encode: EncodingKey,
    pub decode: DecodingKey,
}

impl From<&[u8]> for Keys {
    fn from(value: &[u8]) -> Self {
        Self {
            encode: EncodingKey::from_secret(value),
            decode: DecodingKey::from_secret(value),
        }
    }
}
