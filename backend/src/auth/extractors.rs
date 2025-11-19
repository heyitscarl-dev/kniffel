use axum::{
    extract::FromRequestParts,
    http::{request::Parts, StatusCode},
    RequestPartsExt,
};
use axum_extra::{
    headers::{authorization::Bearer, Authorization},
    TypedHeader,
};

use crate::{app::MutableAppState, services::sessions::SessionID};

/// Extractor for validating session tokens from the Authorization header.
///
/// Usage in handlers:
/// ```rust
/// async fn protected_handler(Session(session_id): Session) -> String {
///     format!("Hello, session: {}", session_id)
/// }
/// ```
pub struct Session(pub SessionID);

impl FromRequestParts<MutableAppState> for Session {
    type Rejection = (StatusCode, String);

    async fn from_request_parts(
        parts: &mut Parts,
        state: &MutableAppState,
    ) -> Result<Self, Self::Rejection> {
        // Extract the Authorization header with Bearer token
        let TypedHeader(Authorization(bearer)) = parts
            .extract::<TypedHeader<Authorization<Bearer>>>()
            .await
            .map_err(|_| {
                tracing::warn!("Authentication failed: Missing or invalid Authorization header");
                (
                    StatusCode::UNAUTHORIZED,
                    "Missing or invalid Authorization header".to_string(),
                )
            })?;

        // Validate the token using the session service
        let session_id = state
            .lock()
            .unwrap()
            .services
            .sessions
            .validate_session(bearer.token().to_string())
            .map_err(|e| {
                tracing::warn!("Authentication failed: Invalid session token - {}", e);
                (
                    StatusCode::UNAUTHORIZED,
                    format!("Invalid session token: {}", e),
                )
            })?;

        tracing::info!("Authentication successful: session_id={:?}", session_id);

        Ok(Session(session_id))
    }
}
