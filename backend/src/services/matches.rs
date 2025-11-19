use std::{collections::HashMap, sync::Arc};

use serde::{Deserialize, Serialize};
use ulid::Ulid;

use crate::services::sessions::{SessionID, SessionService};

#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct MatchID(String);

impl MatchID {
    pub fn new() -> Self {
        Self(Ulid::new().to_string())
    }

    pub fn ulid(&self) -> Ulid {
        Ulid::from_string(&self.0)
            .expect("Expected String contained in SessionID to be valid Ulid.")
    }

    pub fn try_from(string: &str) -> Option<Self> {
        Some(Self(
            Ulid::from_string(string)
                .ok()?
                .to_string()
        ))
    }
}

#[derive(Debug, Clone, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct Match {
    pub id: MatchID,
    pub players: Vec<SessionID>,
}

impl Match {
    pub fn new(players: Vec<SessionID>) -> Self {
        Self {
            id: MatchID::new(),
            players,
        }
    }
}

#[derive(Clone)]
pub struct MatchService {
    sessions: Arc<SessionService>,
    matches: HashMap<MatchID, Match>,
}

impl MatchService {
    pub fn new(sessions: Arc<SessionService>, matches: HashMap<MatchID, Match>) -> Self {
        MatchService { sessions, matches }
    }

    pub fn create_match(&mut self, players: Vec<SessionID>) -> Match {
        let new_match = Match::new(players);
        self.matches.insert(new_match.id.clone(), new_match.clone());
        new_match
    }

    pub fn get_match(&self, match_id: &MatchID) -> Option<&Match> {
        self.matches.get(match_id)
    }

    pub fn delete_match(&mut self, match_id: &MatchID) -> Option<Match> {
        self.matches.remove(match_id)
    }

    pub fn list_matches(&self) -> Vec<&Match> {
        self.matches.values().collect()
    }
}
