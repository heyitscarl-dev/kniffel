use axum::response::IntoResponse;
use hyper::StatusCode;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum Error {
    #[error("Invalid Token Type: \"{}\"", 0)]
    InvalidType(String),

    #[error("Internal Encoding Error")]
    Encoding(#[from] jsonwebtoken::errors::Error),
}

impl Error {
    fn into_status(&self) -> StatusCode {
        match *self {
            Self::InvalidType(_) => StatusCode::BAD_REQUEST,
            Self::Encoding(_) => StatusCode::INTERNAL_SERVER_ERROR
        }
    }
}

impl IntoResponse for Error {
    fn into_response(self) -> axum::response::Response {
        (self.into_status(), self.to_string()).into_response()
    }
}

pub type Result<T> = std::result::Result<T, Error>;
pub type Fallible = Result<()>;
