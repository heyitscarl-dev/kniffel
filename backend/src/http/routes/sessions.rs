use axum::{extract::State, response::IntoResponse, routing::post, Router};

use crate::app::AppState;

pub fn router() -> Router<AppState> {
    Router::new().route("/", post(sessions_root))
}

async fn sessions_root(
    State(state): State<AppState>
) -> impl IntoResponse {
    let session_token = state.services.sessions.issue_session();
    
    if let Ok(session_token) = session_token {
        return session_token;
    }

    return "yeah, no".to_string();
}
