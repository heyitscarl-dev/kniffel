use axum::Router;

pub fn router() -> Router<()> {
    Router::new()
        .nest("/hello", crate::http::routes::hello::router())
        .nest("/sessions", crate::http::routes::sessions::router())
}
