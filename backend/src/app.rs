use std::sync::Arc;

use axum::{extract::FromRef, Router};

use crate::{auth::jwt::Keys, services::sessions::SessionService};

#[derive(Clone)]
pub struct AppState {
    pub services: AppServices
}

impl AppState {
    pub fn new(secret: &str, expire_after_hours: i64) -> Self {
        Self { services: AppServices::new(secret, expire_after_hours) }
    }
}

#[derive(Clone)]
pub struct AppServices {
    pub sessions: SessionService
}

impl AppServices {
    pub fn new(secret: &str, expire_after_hours: i64) -> Self {
        let keys = Arc::new(Keys::new(secret));
        let sessions = SessionService::new(keys, expire_after_hours);
        Self { sessions }
    }
}

impl FromRef<AppState> for AppServices {
    fn from_ref(state: &AppState) -> Self {
        state.services.clone()
    }
}

pub fn router(state: AppState) -> Router {
    Router::new()
        .nest("/hello", crate::http::routes::hello::router())
        .nest("/sessions", crate::http::routes::sessions::router())
        .nest("/protected", crate::http::routes::protected::router())
        .with_state(state)
}
