<!--ai-->
# Agent instructions

- Calendly owns booking pages, calendar conflict detection, confirmations, and Google Meet creation. Do not reimplement them here.
- Read the current Calendly resource before proposing a write.
- Preserve every field the user did not ask to change, especially nested availability rules and booking questions.
- Preview plans with `./calendly apply <file>` before executing them with `--yes`.
- Make one logical change per plan, then read the resource back and verify its public scheduling link.
- Never put a Calendly token, invitee details, or API run reports in Git.
- Do not delete an event type to change its slug or settings. Patch it so existing references keep the same resource identity.
<!--/ai-->

