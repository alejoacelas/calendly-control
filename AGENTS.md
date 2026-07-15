<!--ai-->
# Agent instructions

- Read [API.md](API.md), then open the exact endpoint in Calendly's current API reference before making a request.
- Load `.env` without printing it. Never put the token in a command argument, prompt, log, commit, or response.
- Read the current resource first. Change only requested fields and preserve nested availability rules, locations, and booking questions.
- Use direct HTTPS requests to `https://api.calendly.com`; no local wrapper is needed.
- Retry reads on `429` or `5xx`. Do not automatically retry writes because the first request may have succeeded.
- Do not delete or cancel anything unless the user explicitly asks. Patch event types rather than replacing them.
- After a write, read the resource back and verify the public scheduling link. For availability or conferencing changes, make a test booking with an address the user controls.
<!--/ai-->

