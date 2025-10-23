use std::sync::Arc;

use axum::{routing::get, Router};
use hyper::StatusCode;
use tracing::info;

use crate::{auth::{issue_session, request_session, AuthError, Keychain}, socket::handle_upgrade};

mod socket;
mod auth;

pub const PROTOCOL_VERSION: u32 = 1;
const BIND_ADDRESS: &'static str = "127.0.0.1:3000";

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt::init();

    let secret = std::env::var("JWT_SECRET").expect("JWT secret not set.");
    let keychain = Arc::new(Keychain::from_hs256(secret.as_bytes()));

    let app = Router::new()
        .route("/auth/session", get(request_session))
        .route("/version", get(|| async { PROTOCOL_VERSION.to_string() }))
        .route("/socket", get(handle_upgrade))
        .with_state(keychain);
    
    info!("Starting server on http://{}", BIND_ADDRESS);

    let listener = tokio::net::TcpListener::bind(BIND_ADDRESS).await.unwrap();
    axum::serve(listener, app).await.unwrap();

    Ok(())
}
