use std::sync::{Arc, Mutex};

use axum::{extract::FromRef, Router};

use crate::{auth::jwt::Keys, services::{matches::MatchService, sessions::SessionService}};

pub type MutableAppState = Arc<Mutex<AppState>>;

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
    pub sessions: SessionService,
    pub matches: MatchService,
}

impl AppServices {
    pub fn new(secret: &str, expire_after_hours: i64) -> Self {
        let keys = Arc::new(Keys::new(secret));
        let sessions = SessionService::new(keys, expire_after_hours);
        let matches = MatchService::new(Arc::new(sessions.clone()), Default::default());
        Self { sessions, matches }
    }
}

impl FromRef<AppState> for AppServices {
    fn from_ref(state: &AppState) -> Self {
        state.services.clone()
    }
}

pub fn router(state: Arc<Mutex<AppState>>) -> Router {
    Router::new()
        .nest("/hello", crate::http::routes::hello::router())
        .nest("/auth", crate::http::routes::sessions::router())
        .nest("/protected", crate::http::routes::protected::router())
        .with_state(state)
}
