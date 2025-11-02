use std::sync::Arc;

use axum::{extract::State, routing::get, Json, Router};
use serde::{Deserialize, Serialize};
use tracing::info;

use crate::{
    auth::{request_token, Keys, Token}, socket::handle_upgrade
};

mod auth;
mod socket;

pub const PROTOCOL_VERSION: u32 = 1;
const BIND_ADDRESS: &'static str = "127.0.0.1:3000";

#[derive(Serialize, Deserialize)]
struct ProtectedParams {
    token: String
}

async fn protected(
    State(keys): State<Arc<Keys>>,
    Json(params): Json<ProtectedParams>
) -> crate::auth::Result<String> {
    let _claims = auth::verify_session(&keys, params.token)?;

    Ok("all good :)".to_owned())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt::init();

    let secret = std::env::var("JWT_SECRET").expect("JWT secret (env: JWT_SECRET) not set.");
    let keys = Arc::new(secret.as_bytes().into());

    let app = Router::new()
        .route("/auth", get(request_token))
        .route("/protected", get(protected))
        .route("/socket", get(handle_upgrade))
        .route("/version", get(|| async { PROTOCOL_VERSION.to_string() }))
        .with_state(keys);

    info!("Starting server on http://{}", BIND_ADDRESS);

    let listener = tokio::net::TcpListener::bind(BIND_ADDRESS).await.unwrap();
    axum::serve(listener, app).await.unwrap();

    Ok(())
}
