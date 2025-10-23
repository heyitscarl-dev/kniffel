# Protocol

## High-Level Flow

_Before_

1. Connect
2. Authenticate
3. (Join or Create) Match

**Loop**:
1. Up to three rolls, hold/unhold dice after each roll
2. Choose scoring category

_After_

4. Evaluate

## Packets

| Client-Side Request   | Server-Side Response      | Server-Side Broadcast | Client-Side Response  |
| --------------------- | ------------------------- | --------------------- | --------------------- |
| `Authenticate`        | `AuthOk` or `AuthErr`     |                       |                       |
| `CreateMatch`         | `MatchOk` and `Match`     |                       |                       |
| `JoinMatch`           | `JoinOk` and `Match`      | `JoinedMatch`         |                       |
| `ResumeMatch`         | `ResumeOk` and `Match`    | `JoinedMatch`         |                       |
| `DisbandMatch`        |                           | `DisbandedMatch`      |                       |
| `LeaveMatch`          |                           | `LeftMatch`           |                       |
| `Ready`               | `ReadyOk`                 | `Readied`             |                       |
| `Roll`                | `RollOk`                  | `Rolled`              |                       |
| `Hold`                | `HoldOk`                  | `Held`                |                       |
| `Score`               | `ScoreOk`                 | `Scored`              |                       |
| `Ping`                | `Pong`                    |                       |                       |
|                       |                           | `Match`               |                       |
|                       |                           | `AdvanceTurn`         |                       |
|                       |                           | `StartGame`           |                       |
|                       |                           | `GameOver`            |                       |
|                       | `ClientError`             |                       |                       |
|                       |                           | `ServerError`         |                       |
|                       |                           | `Ping`                | `Pong`                |
| `Disconnect`          |                           | `Disconnected`        | `Wait` or `Claim`     |
