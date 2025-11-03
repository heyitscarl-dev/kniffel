pub mod model;
use std::{collections::HashMap, str::FromStr};

use axum::{extract::State, Json};
pub use model::*;
use serde::{Deserialize, Serialize};
use tracing::info;
use ulid::Ulid;
use uuid::Uuid;

use crate::{auth::{self, verify_session, Token}, AppState};

#[derive(Debug, Serialize, Deserialize)]
pub struct NewMatchParams {
    token: String
}

pub async fn new_match(
    State((matches, keys)): State<AppState>,
    Json(params): Json<NewMatchParams>,
) -> auth::Result<String> {
    let claims = verify_session(&keys, Token::new(params.token))?;

    let id = Uuid::new_v4();
    let mut players = HashMap::new();
    let player_id = Uuid::from_str(&claims.sub).unwrap();
    let player = LobbyPlayerState { ready: false };
    players.insert(player_id, player);


    {
        matches.lock().unwrap().insert(id, Match { data: MatchData::Lobby(LobbyMatch {
            players
        })});
    }

    info!("New match {} with player {}.", id.to_string(), claims.sub);

    Ok(id.to_string())
}
