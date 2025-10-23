# Auth (Authentication, Authorization)

On startup, the client sends an `Auth` request to the server (at `/auth/annonymous` or similar). The server responds with a **session-token**, valid for 24h, which resembles a user id. 

Then, when the player joins a match, it sends a `JoinMatch` request to the server, which issues a **match capability token**
