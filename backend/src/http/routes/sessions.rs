use axum::{extract::State, response::IntoResponse, routing::get, Router};

use crate::app::AppState;

pub fn router() -> Router<AppState> {
    Router::new().route("/", get(sessions_root))
}

async fn sessions_root(
    State(state): State<AppState>
) -> impl IntoResponse {
    tracing::info!("Session token requested");

    let session_token = state.services.sessions.issue_session();

    if let Ok(session_token) = session_token {
        tracing::info!("Session token issued successfully");
        return session_token;
    }

    tracing::error!("Failed to issue session token: {:?}", session_token);
    return "yeah, no".to_string();
}
