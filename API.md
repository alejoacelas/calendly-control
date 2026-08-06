---
human_edit_tracking:
  enabled: true
  history: []
---
# Calendly API

Checked 2026-07-15 against Calendly API v2 and the live account.

## Start here

- [API reference](https://developer.calendly.com/api-docs): request and response schemas. Search for the endpoint by resource and operation before calling it.
- [Scope catalog](https://developer.calendly.com/scopes): current permissions and the endpoints each scope authorizes.
- [Getting started](https://developer.calendly.com/getting-started): authentication, plans, roles, API v2, embeds, and webhooks.
- [Release notes](https://developer.calendly.com/release-notes): new endpoints and behavior changes. Check this when this file is old.
- [API use cases](https://developer.calendly.com/api-use-cases): availability, booking, reporting, embeds, and sharing recipes.
- [Supported MCP tools](https://developer.calendly.com/supported-tools): concise endpoint inventory, useful even when calling REST directly.
- [Calendly MCP](https://developer.calendly.com/calendly-mcp-server): optional hosted MCP at `https://mcp.calendly.com`. It requires OAuth 2.1, PKCE, and Dynamic Client Registration; local Codex and Claude clients failed its callback flow on 2026-07-15, so this project uses the PAT directly.

Base URL: `https://api.calendly.com`

## Authentication

`secretspec.toml` declares `CALENDLY_TOKEN`; its value lives in the `Developer-Credentials` 1Password vault. SecretSpec injects it only into the request process:

```sh
secretspec run --reason "Read the current Calendly user" -- sh -c '
  curl --fail-with-body --silent --show-error --max-time 30 \
    -H "Authorization: Bearer $CALENDLY_TOKEN" \
    -H "Accept: application/json" \
    https://api.calendly.com/users/me | jq
'
```

Change the reason to match the request. Never use `set -x`, retrieve the token with `secretspec get`, put it directly in a command, or paste it into chat. If the token appears in a prompt or log, revoke it at [API & Webhooks](https://calendly.com/integrations/api_webhooks), replace the 1Password item, and assume the old value is compromised.

Install the prerequisites with `brew install --cask 1password 1password-cli` and `cargo install secretspec --locked`, then enable **1Password → Settings → Developer → Integrate with 1Password CLI**. To roll back, copy `.env.example` to `.env`, add the token, and use the former `source .env` flow; `.env` remains gitignored.

For a write, copy the exact body from the current API reference. Read the resource first, send the smallest supported `PATCH`, then read it again. Do not infer a payload from an older example.

## What the API can do

As of 2026-07-15:

- Event types: list and read existing types and available times; create or update standard and one-off event types, including names, slugs, durations, locations, buffers, booking questions, and other supported settings.
- Availability: read schedules, date overrides, busy times, and bookable slots; update an event type's availability schedule.
- Bookings: list scheduled events and invitees, create an invitee booking, cancel an event, and mark or clear no-shows. There is no direct reschedule endpoint; use the returned reschedule URL or cancel and create deliberately.
- Links: read public scheduling URLs and create ordinary or customized single-use scheduling links.
- Conferencing: list connected meeting locations and assign supported existing locations such as Google Meet to event types. Connecting the Google account itself remains a Calendly UI action.
- Routing: read routing forms and submissions. The current public scope catalog exposes no routing-form write scope.
- Organization: read groups, memberships, invitations, and organizations; invite or remove organization members where the authenticated account's role permits it.
- Contacts: list, read, create, update, and delete contacts.
- Webhooks: list, inspect, create, and delete webhook subscriptions. Calendly says webhook access requires a paid plan.
- Operations and compliance: read activity logs and outgoing communications; request invitee or scheduled-event data deletion.

API access is still bounded by Calendly's current endpoint behavior, subscription, and the authenticated user's organization role. A token scope does not override those limits.

## This token's permissions

The PAT stored in 1Password was decoded locally and verified with read-only calls to `/users/me` and `/event_types` on 2026-07-15. It contains every scope in Calendly's current public PAT catalog:

- Scheduling: `availability:read`, `availability:write`, `event_types:read`, `event_types:write`, `locations:read`, `routing_forms:read`, `shares:write`, `scheduled_events:read`, `scheduled_events:write`, `scheduling_links:write`.
- Account: `groups:read`, `organizations:read`, `organizations:write`, `users:read`.
- Contacts: `contacts:read`, `contacts:write`.
- Webhooks: `webhooks:read`, `webhooks:write`.
- Security and operations: `activity_log:read`, `data_compliance:write`, `outgoing_communications:read`.

The token can therefore perform every operation currently authorized by a public PAT scope, including destructive contact, membership, webhook, cancellation, and compliance operations. Access to its 1Password item is effectively account administration. Prefer a narrower replacement token once the recurring workflows are known.

## Request discipline

1. Check the release notes and exact endpoint reference if this file's date is stale.
2. Read `/users/me`, then resolve resource URIs from API responses instead of constructing IDs from public links.
3. Save no invitee, contact, or event responses in this repository; they contain information from other people.
4. Treat `401` as an expired or revoked token, `403` as a scope/role/plan mismatch, `404` as a stale URI, `429` as a retry-after signal, and `5xx` as transient.
5. Retry `GET` requests with bounded exponential backoff. Never automatically retry `POST`, `PUT`, `PATCH`, or `DELETE`.
6. Make one logical change, read it back, and test its public booking flow before starting another.
