# Backend Implementation Roadmap

## Current Status
- [x] Session authentication (GET /auth)
- [x] Session token generation and validation
- [x] Session extractor for protected endpoints

## Next Stage: Match Management & Capability Tokens

### Phase 1: Core Match Service
**Goal**: Implement match creation, storage, and lifecycle management

**Tasks**:
1. Create `services/matches.rs` module
   - Define `Match` struct (match_id, access_code, player1_session, player2_session, status)
   - Define `MatchStatus` enum (Waiting, Ready, InProgress, Completed)
   - Implement access code generation (6-char alphanumeric, human-readable)

2. Implement `MatchService` with thread-safe storage
   - Use `Arc<RwLock<HashMap<MatchId, Match>>>` for match storage
   - Use `Arc<RwLock<HashMap<AccessCode, MatchId>>>` for lookup by code

3. Add match lifecycle methods:
   - `create_match(session_id: SessionID) -> Result<(MatchId, AccessCode)>`
   - `get_match_by_code(access_code: &str) -> Result<Match>`
   - `join_match(match_id: MatchId, session_id: SessionID) -> Result<()>`
   - `mark_ready(match_id: MatchId, session_id: SessionID) -> Result<()>`
   - `is_match_ready(match_id: MatchId) -> Result<bool>`

4. Add match service to `AppServices` in `app.rs`

### Phase 2: Capability Token System
**Goal**: Extend auth system to support match-specific capability tokens

**Tasks**:
1. Extend `auth/claims.rs`:
   - Add `ClaimsType::Capability` variant
   - Add optional `match_id` field to `Claims` struct

2. Extend `SessionService` (or create `CapabilityService`):
   - `issue_capability(session_id: SessionID, match_id: MatchId) -> Result<String>`
   - `validate_capability(token: String) -> Result<(SessionID, MatchId)>`

3. Create `Capability` extractor in `auth/extractors.rs`:
   - Similar to `Session` extractor
   - Returns `Capability(SessionID, MatchId)` tuple
   - Validates both session and match access

### Phase 3: REST Endpoints
**Goal**: Implement match-related HTTP endpoints per protocol

**Tasks**:
1. Create `http/routes/matches.rs`:
   - `POST /matches` - Create match, return capability token
     - Input: Session extractor
     - Output: `{ match_id, access_code, capability_token }`

   - `GET /matches?code={access_code}` - Lookup match by code
     - Input: Query parameter, Session extractor
     - Output: `{ match_id, capability_token }`

   - `POST /matches/join` - Join a match
     - Input: `{ match_id }` in body, Session extractor
     - Output: `{ capability_token }`

   - `POST /matches/ready` - Mark player as ready
     - Input: Capability extractor
     - Output: `{ ready: bool, match_ready: bool }`

2. Mount routes in `app.rs`:
   - `.nest("/matches", crate::http::routes::matches::router())`

### Phase 4: Error Handling & Validation
**Goal**: Robust error handling for match operations

**Tasks**:
1. Create `services/matches/error.rs`:
   - `MatchNotFound`
   - `MatchAlreadyFull`
   - `AlreadyInMatch`
   - `NotInMatch`
   - `InvalidAccessCode`

2. Add proper HTTP status code mapping:
   - 404 for not found
   - 409 for conflicts (already joined, already full)
   - 403 for unauthorized match access

### Phase 5: Testing
**Goal**: Ensure match system works correctly

**Tasks**:
1. Unit tests for `MatchService`:
   - Create match generates unique access codes
   - Join match adds player correctly
   - Can't join full match
   - Both players ready triggers match ready state

2. Integration tests for endpoints:
   - Full flow: create → join → ready → ready
   - Error cases: invalid codes, unauthorized access
   - Capability token validation

3. Manual testing:
   - Use `curl` or HTTP client to test full player flow
   - Verify tokens work correctly

## Future Stages

### Stage 3: WebSocket Connection & Game Loop
- WebSocket server setup
- Connection authentication with capability tokens
- Match start coordination
- Game state management

### Stage 4: Game Logic
- Dice rolling mechanics
- Score calculation
- Turn management
- Win conditions

## Notes
- Keep separation between service layer (business logic) and HTTP layer (routing/serialization)
- Use proper error types, avoid string errors
- Follow conventional commits format
- Update protocol.md if API design changes
