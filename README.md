<!--ai-->
# Calendly

Calendly runs the booking pages, calendar conflict checks, confirmations, and Google Meet links. This folder makes the account operable from Codex, Claude Code, or a shell.

## Connect

1. Keep using your existing Calendly account. A Standard subscription is the sensible default when you need multiple meeting types; Free is enough for one.
2. In Calendly, connect Google Calendar and select Google Meet on each meeting type.
3. Create a [personal access token](https://calendly.com/integrations/api_webhooks) with `users:read`, `event_types:write`, `availability:write`, and `locations:read`.
4. Copy `.env.example` to `.env` and put the token there. `.env` is ignored by Git.

```sh
cp .env.example .env
./calendly doctor
./calendly links
```

`doctor` and `links` are read-only. The token never appears in output.

## Change Calendly

Use the hosted Calendly MCP server in Claude Code. This repository's `.mcp.json` points Claude at `https://mcp.calendly.com`; approve it and sign in when Claude asks. Examples:

```text
List my Calendly event types and their links.
Remove Fridays from my 30-minute meeting availability.
Change my intro meeting slug to intro and keep every other setting unchanged.
```

Codex's current OAuth callback is rejected by Calendly, so use the local CLI from Codex until that client incompatibility is fixed. Read any endpoint:

```sh
./calendly get /users/me
./calendly get /event_types --query user=https://api.calendly.com/users/USER_ID
```

For writes, put exact API requests in a plan. Preview is the default; `--yes` executes:

```sh
cp config/change.example.json config/change.json
$EDITOR config/change.json
./calendly apply config/change.json
./calendly apply config/change.json --yes
```

Each executed run writes a redacted report under `history/runs/`. The directory is ignored because API responses can contain information about other people.

## Test

```sh
python3 -m unittest discover -s tests -v
```

See [RESEARCH.md](RESEARCH.md) for the provider comparison and [docs/operations.md](docs/operations.md) for safety and recovery.
<!--/ai-->

