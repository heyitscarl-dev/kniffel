use axum::{
    extract::{ws::{CloseFrame, Message, WebSocket}, WebSocketUpgrade}, response::IntoResponse, routing::get, Router
};

pub const PROTOCOL_VERSION: u32 = 1;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/version", get(version))
        .route("/socket", get(handle_upgrade));

    // run our app with hyper, listening globally on port 3000
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

async fn handle_upgrade(ws: WebSocketUpgrade) -> impl IntoResponse {
    ws.on_failed_upgrade(|error| println!("Failed Upgrade: {}", error))
        .on_upgrade(handle_socket)
}

async fn handle_socket(mut socket: WebSocket) {
    while let Some(msg) = socket.recv().await {
        if let Ok(msg) = msg {
            match msg {
                Message::Text(utf8_bytes) => {
                    println!("Text received: {}", utf8_bytes);
                    let result = socket.send(Message::Text(
                        format!("Echo: {}", utf8_bytes).into()
                    )).await;
                    if let Err(error) = result {
                        println!("Error sending: {}", error);
                        send_close_message(socket, 1011, &format!("Error occured: {}", error)).await;
                        break;
                    }
                },
                Message::Binary(bytes) => {
                    println!("Received bytes of length: {}", bytes.len());
                    let result = socket
                        .send(Message::Text(
                            format!("Received bytes of length: {}", bytes.len()).into(),
                        ))
                        .await;
                    if let Err(error) = result {
                        println!("Error sending: {}", error);
                        send_close_message(socket, 1011, &format!("Error occured: {}", error))
                            .await;
                        break;
                    }
                },
                _ => {}
            }
        }
    }
}

async fn send_close_message(mut socket: WebSocket, code: u16, reason: &str) {
    _ = socket
        .send(Message::Close(Some(CloseFrame {
            code: code,
            reason: reason.into(),
        })))
        .await;
}

// basic handler that responds with a static string
async fn version() -> String {
    PROTOCOL_VERSION.to_string()
}

