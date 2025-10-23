use axum::{routing::get, Router};

use crate::socket::handle_upgrade;

pub const PROTOCOL_VERSION: u32 = 1;

mod socket;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/socket", get(handle_upgrade));

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
