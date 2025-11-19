use axum::{extract::State, response::IntoResponse, routing::get, Router};

use crate::app::MutableAppState;

pub fn router() -> Router<MutableAppState> {
    Router::new().route("/", get(sessions_root))
}

async fn sessions_root(
    State(state): State<MutableAppState>
) -> impl IntoResponse {
    tracing::info!("Session token requested");

    let session_token = {
        let state = state.lock().unwrap();
        state.services.sessions.issue_session()
    };

    if let Ok(session_token) = session_token {
        tracing::info!("Session token issued successfully");
        return session_token.into_response();
    }

    tracing::error!("Failed to issue session token: {:?}", session_token);
    return session_token.unwrap_err().into_response();
}
