use axum::{response::IntoResponse, routing::get, Router};

pub fn router() -> Router<()> {
    Router::new()
        .route("/", get(sessions_root))
}

async fn sessions_root() -> impl IntoResponse {
    "{ error: \"unimplemented 500\" }"
}
