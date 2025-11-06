use axum::{extract::Path, response::IntoResponse, routing::get, Json, Router};
use serde::Serialize;

use crate::app::AppState;

#[derive(Serialize)]
pub struct HelloResponse {
    message: String
}

pub fn router() -> Router<AppState> {
    Router::new()
        .route("/", get(root_hello))
        .route("/{name}", get(hello_name))
}

async fn root_hello() -> impl IntoResponse {
    let msg = "hello world!".to_string();
    Json(HelloResponse { message: msg })
}

async fn hello_name(
    Path(name): Path<String>,
) -> impl IntoResponse {
    let msg = format!("hello {}!", name);
    Json(HelloResponse { message: msg })
}
