---
agent_context:
  version: 1
  groups:
  - tools
  visibility: public
---
<!-- agent-context:begin sha256=cb545175271c3a7242acaa4371e2a433d4fe8566eab054e57071cef6a99bde12 -->
<!-- shared group: tools -->
# Dev Workspace

- This workspace holds software the user relies on frequently. Build it to last, not as throwaway experiments.
- Group related projects under an ordinary shared-function folder whose README indexes them; do not also use that folder as a project repo.
- Keep each project in its own Git repo with its own GitHub remote, including nested projects.
- Commit project work inside its project repo; keep shared workspace config in dotfiles.
- Push after committing.
- Keep changes small.

## Publishing a project

- Create the GitHub remote if it doesn't exist.
- Use a short, clean repo name.
- Make the repo public unless the global privacy rules require a private repo.

## READMEs

- Put real effort into the README.
- Keep it short — write it like a WhatsApp or Slack message, straight to the point.
- If it can be said in one sentence, don't use two.
- When the user's prompt has its own wording and style, preserve that voice; just make it shorter and tighter.
- Write in the user's own first-person voice — a short, honest personal note, not marketing copy.

## Local macOS apps

- Sign apps that need Accessibility, Screen Recording, microphone, camera or similar grants with a stable local identity. Ad-hoc signatures change identity on every build, leaving enabled privacy toggles that the rebuilt app cannot use.
- Make the build fail when its expected signing identity is missing. Do not silently fall back to ad-hoc signing.

## Markdown

- Use [Peter Hartree's Roughdraft fork](https://github.com/peterhartree/roughdraft) as the default Markdown review tool.
- Open files with `roughdraft open "/absolute/path/to/file.md"`.
- After the user reviews or closes a document, reread the file for CriticMarkup feedback.
<!-- agent-context:end -->

# Agent instructions

- Read [API.md](API.md), then open the exact endpoint in Calendly's current API reference before making a request.
- Run API commands through SecretSpec, which loads `CALENDLY_TOKEN` from the `Developer-Credentials` 1Password vault. State the specific reason with `--reason`. Never retrieve, print, or put the token in a command argument, prompt, log, commit, or response.
- Read the current resource first. Change only requested fields and preserve nested availability rules, locations, and booking questions.
- Use direct HTTPS requests to `https://api.calendly.com`; no local wrapper is needed.
- Retry reads on `429` or `5xx`. Do not automatically retry writes because the first request may have succeeded.
- Do not delete or cancel anything unless the user explicitly asks. Patch event types rather than replacing them.
- After a write, read the resource back and verify the public scheduling link. For availability or conferencing changes, make a test booking with an address the user controls.
