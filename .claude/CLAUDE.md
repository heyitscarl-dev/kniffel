# Kniffel Project Instructions

## Project Overview
This is a Kniffel (Yahtzee) game implementation with a Rust backend.

## Code Style & Conventions

### Rust
- Follow standard Rust idioms and conventions
- Use `thiserror` for custom error types
- Prefer `Result<T, E>` for fallible operations
- Use async/await with Tokio runtime
- Keep module structure clean with proper `mod.rs` files

### Error Handling
- Use the common error module for shared error types
- Authentication errors should use dedicated auth error types
- Provide descriptive error messages
- Use proper HTTP status codes in API responses

### Testing
- Write unit tests for business logic
- Write integration tests for HTTP endpoints
- Test authentication flows thoroughly
- Use `cargo test` to run all tests

## Authentication System
- Session tokens with 24-hour validity
- Capability tokens for match-specific access
- Token validation on protected endpoints
- Refer to `/backend/docs/authorization.md` for detailed auth flow

## API Design
- Follow REST principles for HTTP endpoints
- Use proper HTTP methods and status codes
- Refer to `/backend/docs/protocol.md` for API specification

## Development Workflow

### Building
```bash
cd backend
cargo build
```

### Running
```bash
cd backend
cargo run
```

### Testing
```bash
cd backend
cargo test
```

### Linting
```bash
cd backend
cargo clippy
```

## Important Notes
- Always use conventional commits format (e.g., `feat:`, `fix:`, `refactor:`)
- Check protocol and authorization docs before implementing new endpoints
- Maintain separation between auth, services, and HTTP layers
- Keep error handling DRY and consistent
