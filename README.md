# calendly

Calendly hosts the booking pages, availability checks, invitations, and Google Meet links. Agents change it through the official API using a token retrieved from 1Password with `op` into a Git-ignored, owner-only `.env`.

Read [API.md](API.md) before touching the account. It records the current API surface, token permissions, documentation links, and safe request pattern.

## Credential

`CALENDLY_TOKEN` authenticates requests to Calendly API v2. This is a personal
integration: explicitly select `my.1password.com` (`alejoacelas@gmail.com`) in `op`.
The old setup named vault `Developer-Credentials`, but that vault was absent from
this account on 2026-09-19 and no Calendly-named item was found. The current vault,
item and field are **unverified**; confirm them and record their identifiers here
before retrieving a key. Do not copy a work-account credential into this project.

Before creating `.env`, verify it is ignored and untracked, and set mode 600 before
writing secret values. Reuse the local file for subsequent requests. Never commit
or print its contents. `secretspec.toml` is a legacy configuration, not the current
credential workflow.
