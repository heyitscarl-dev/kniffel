use crate::app::AppState;

mod app;
mod auth;
mod http;
mod common;
mod services;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let state = AppState::new("thisisasupersecretsecret", 12);
    let app = app::router(state);

    let addr = "127.0.0.1:3000";
    tracing::info!("Listening on http://{addr}");

    let listener = tokio::net::TcpListener::bind(addr)
        .await
        .expect("Could not bind to port.");

    axum::serve(listener, app)
        .await
        .expect("Could not serve.")
}
