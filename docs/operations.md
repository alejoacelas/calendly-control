<!--ai-->
# Operations

## Safety model

- Read commands retry rate limits and transient server errors up to three times.
- Write commands never retry automatically. A timed-out create can have succeeded even when the response was lost.
- `apply` previews by default and requires `--yes` to write.
- Plans reject absolute URLs, path traversal, non-HTTPS API bases, and destructive HTTP methods unless the operation also sets `allow_destructive: true`.
- A non-Calendly API base also requires `CALENDLY_ALLOW_CUSTOM_API_BASE=1`, preventing an accidental configuration change from sending the token elsewhere.
- Execution stops on the first failed operation. Earlier operations may already have succeeded; inspect the run report before retrying.
- Tokens are read from the environment or `.env`, never command-line arguments, and authorization headers are never logged.

## Recovery

Before a risky change, save the current resource:

```sh
./calendly get /event_types/EVENT_TYPE_ID > before.json
```

Use `PATCH`, not delete-and-create, for slugs, durations, descriptions, locations, and availability. This preserves the event type identity and limits link breakage.

Availability updates replace nested rules. Read the current schedule first and carry every unchanged rule into the plan; the placeholder in `config/change.example.json` is deliberately invalid until replaced with the complete array.

After a write:

1. Run `./calendly links` and the matching `get` command.
2. Open the public scheduling link in a private browser window.
3. Confirm the intended timezone, next available slots, and Google Meet location.
4. Make one end-to-end test booking with an email address you control, then cancel it.

## Agent rule

Agents should read the current resource, change only the requested fields, preview the plan, execute one logical change, and verify the resulting public link. Do not replace whole nested arrays such as booking questions or availability rules without preserving unmodified entries.
<!--/ai-->
