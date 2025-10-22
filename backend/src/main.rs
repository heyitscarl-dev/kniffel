use axum::{
    routing::get,
    Router
};

pub const PROTOCOL_VERSION: u32 = 1;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/version", get(version));

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

// basic handler that responds with a static string
async fn version() -> String {
    PROTOCOL_VERSION.to_string()
}
