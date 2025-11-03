use std::{
    collections::{BTreeMap, HashMap},
    time::SystemTime,
};

use uuid::Uuid;

pub struct Match {
    pub data: MatchData,
}

pub enum MatchData {
    Lobby(LobbyMatch),
    Active(ActiveMatch),
    Finished(FinishedMatch),
}

pub struct LobbyMatch {
    pub players: HashMap<Uuid, LobbyPlayerState>,
}

pub struct LobbyPlayerState {
    pub ready: bool,
}

pub struct ActiveMatch {
    pub players: HashMap<Uuid, ActivePlayerState>,
    pub turn_index: usize,
    pub roll_index: usize,
    pub dice: [u8; 5],
    pub kept: [bool; 5],
}

pub struct ActivePlayerState {
    pub scores: ScoreSheet,
}

pub struct ScoreSheet {
    pub categories: BTreeMap<Category, Option<u16>>,
}

pub enum Category {
    Ones,
    Twos,
    Threes,
    Fours,
    Fives,
    Sixes,

    ThreeOfAKind,
    FourOfAKind,
    FullHouse,

    SmallStraight,
    LargeStraight,

    Kniffel,
    Chance,
}

pub struct FinishedMatch {
    pub players: HashMap<Uuid, FinishedPlayerState>,
    pub winners: Vec<Uuid>,
}

pub struct FinishedPlayerState {
    pub scores: ScoreSheet,
}
