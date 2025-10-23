use axum::{extract::{ws::{CloseFrame, Message, Utf8Bytes, WebSocket}, WebSocketUpgrade}, response::IntoResponse};

fn handle_upgrade_failure(error: axum::Error) {
    eprintln!("Failed to upgrade protocol: {}", error)
}

pub async fn handle_upgrade(upgrade: WebSocketUpgrade) -> impl IntoResponse {
    upgrade.on_failed_upgrade(handle_upgrade_failure)
        .on_upgrade(handle_socket)
}

async fn handle_socket(mut socket: WebSocket) {
    while let Some(message) = socket.recv().await {
        if let Ok(message) = message {
            handle_message(&mut socket, message).await;
        }
    }
}

async fn handle_message(socket: &mut WebSocket, message: Message) {
    match message {
        Message::Text(utf8) => handle_text(socket, utf8).await,
        Message::Binary(_) => send_close_unsupported(socket).await,
        _ => {}
    }
}

async fn handle_text(socket: &mut WebSocket, utf8: Utf8Bytes) {
    println!("{}", utf8)
}

const CODE_CLOSE_UNSUPPORTED: u16 = 1003;

async fn send_close_unsupported(socket: &mut WebSocket) {
    send_close(socket, CODE_CLOSE_UNSUPPORTED, format!("This connection only supports Text based communication!")).await
}

async fn send_close(socket: &mut WebSocket, code: u16, reason: String) {
    let _ = socket.send(Message::Close(Some(CloseFrame {
        code: code,
        reason: reason.into()
    })));
}
