# Calendly administration decisions

## Core decisions

### Access

- [Use direct API requests and verify the personal credential location](#decision-1).

### Safe changes

- [Read before changing only the requested fields](#decision-2).
- [Do not automatically retry writes and verify their result](#decision-3).

## Details

<a id="decision-1"></a>

### Use direct API requests and verify the personal credential location

The project is account-administration guidance, not a local wrapper. Current instructions use op and an ignored owner-only .env; the formerly named vault was absent and the item/field remain unverified. Do not borrow a work credential or treat legacy secretspec.toml as current setup. See [README.md](README.md).

<a id="decision-2"></a>

### Read before changing only the requested fields

Inspect the exact current API endpoint and resource. Preserve nested availability, locations and questions, patch event types rather than replacing them, and require an explicit request before deletion or cancellation. See [AGENTS.md](AGENTS.md).

<a id="decision-3"></a>

### Do not automatically retry writes and verify their result

Retrying a failed-looking write can duplicate a successful operation. Read back changes and check the public scheduling link; availability or conferencing changes need an authorized test booking with a controlled address. See [API.md](API.md). History inspected: [9b98b8b](https://github.com/alejoacelas/calendly-control/commit/9b98b8b).
