use axum::{routing::get, Router};

use crate::{app::MutableAppState, auth::extractors::Session};

pub fn router() -> Router<MutableAppState> {
    Router::new()
        .route("/", get(protected_handler))
}

/// Example protected endpoint that requires session authentication.
/// The Session extractor will automatically validate the Authorization header.
async fn protected_handler(
    Session(session_id): Session
) -> String {
    tracing::debug!("Protected endpoint accessed by session: {:?}", session_id);
    format!("Hello, authenticated session: {:?}", session_id)
}
