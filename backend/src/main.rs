use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};

use axum::{routing::{get, post}, Router};
use tracing::info;
use uuid::Uuid;

use crate::{auth::{request_token, Keys}, r#match::{new_match, Match}, socket::handle_upgrade};

mod auth;
mod r#match;
mod socket;

pub const PROTOCOL_VERSION: u32 = 1;
const BIND_ADDRESS: &'static str = "127.0.0.1:3000";

pub type Matches = Arc<Mutex<HashMap<Uuid, Match>>>;
pub type AppState = (Matches, Arc<Keys>);

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    tracing_subscriber::fmt::init();

    let secret = std::env::var("JWT_SECRET").expect("JWT secret (env: JWT_SECRET) not set.");
    let keys = Arc::new(secret.as_bytes().into());

    let matches: Matches = Arc::new(Mutex::new(HashMap::new()));

    let app = Router::new()
        .route("/matches", post(new_match))
        .route("/auth", get(request_token))
        .route("/socket", get(handle_upgrade))
        .route("/version", get(|| async { PROTOCOL_VERSION.to_string() }))
        .with_state((matches, keys));

    info!("Starting server on http://{}", BIND_ADDRESS);

    let listener = tokio::net::TcpListener::bind(BIND_ADDRESS).await.unwrap();
    axum::serve(listener, app).await.unwrap();

    Ok(())
}
