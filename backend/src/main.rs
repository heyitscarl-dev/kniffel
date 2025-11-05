mod common;
mod http;
mod app;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    let app = app::router();

    let addr = "127.0.0.1:3000";
    tracing::info!("Listening on http://{addr}");

    let listener = tokio::net::TcpListener::bind(addr)
        .await
        .expect("Could not bind to port.");

    axum::serve(listener, app)
        .await
        .expect("Could not serve.")
}
