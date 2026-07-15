<!--ai-->
# Scheduling provider comparison

Research checked 2026-07-15. Prices are monthly per user unless stated otherwise; annual billing can be cheaper.

## Recommendation

Keep Calendly. It now combines the two requirements that previously forced a tradeoff: a mature hosted booking service and supported write access for agents. Its API can create and update event types and availability, while its hosted MCP server exposes those operations directly to compatible AI clients. Calendly's public status page showed 100% uptime for calendly.com and API/webhooks for the displayed Apr–Jul 2026 window.

Use Standard at $10/user/month billed annually when you need more than one event type, multiple calendars, reminders, or webhooks. Free still supports one event type, Google Meet, and API access. The threshold for switching is concrete: reconsider SavvyCal if its calendar-overlay booking UX matters more than Calendly's operating history, or Cal.com if open-source portability matters more than the incident history below.

## Options

| Service | Hosted booking + Google Meet | Agent/terminal control | Price worth testing | Main tradeoff |
|---|---|---|---:|---|
| [Calendly](https://calendly.com/pricing) | Yes | Official [REST API](https://developer.calendly.com/scopes) and [hosted MCP](https://developer.calendly.com/calendly-mcp-server) can update event types and availability | Free; Standard $10 annually | Best fit. MCP requires dynamic OAuth registration, which not every client implements correctly. |
| [SavvyCal](https://savvycal.com/pricing) | Yes | Its [API](https://developers.savvycal.com/api/scheduling-links) can create, update, duplicate, disable, and delete scheduling links | Basic $12 | Strong API and an excellent invitee calendar-overlay UI; smaller vendor and no published reliability figure found. |
| [Cal.com](https://cal.com/pricing) | Yes | Broad [API v2](https://cal.com/docs/api-reference/v2/event-types/update-an-event-type), open source, and self-host escape hatch | Free; Teams $12 annually | Most portable. Its public incident history includes booking-page, email, API, and database incidents in 2025–26, so it is not the first choice for this reliability requirement. |
| [Nylas Scheduler](https://developer.nylas.com/docs/v3/scheduler/) | Yes | API-first configurations and [Nylas-hosted pages](https://developer.nylas.com/docs/v3/scheduler/hosted-scheduling-pages/) | Contact sales after trial | Best when scheduling is embedded in another product. More integration surface and account plumbing than a personal booking link needs. |
| [Cronofy](https://www.cronofy.com/pricing) | Yes | Scheduler API and embedded components | Team $15; API access starts with Business at $799/month annually | Publishes a 99.99% uptime guarantee, but API pricing is disproportionate for one person's links. |

## Reliability evidence

- [Calendly status](https://calendlystatus.com/) reports separate booking-site, notification, calendar-integration, and API/webhook components. The displayed Apr–Jul 2026 window reported 100% for the booking site and API/webhooks.
- [Cal.com incident history](https://status.cal.com/events?filter=reports) records a five-hour partial booking-link outage in May 2026, delayed notifications/webhooks in June 2026, API gateway timeouts in June 2026, and earlier email/database incidents.
- [Cronofy pricing](https://www.cronofy.com/pricing) states a 99.99% uptime guarantee. The guarantee is useful evidence, but its $799/month API tier changes the decision for this single-user use case.
- SavvyCal and Nylas documentation describes capabilities, but I found no comparable public uptime percentage or contractual SLA for their entry plans. Measure successful synthetic bookings before using either as a failover.

## Experiment links

- [Calendly signup or subscription](https://calendly.com/signup)
- [SavvyCal signup](https://savvycal.com/signup)
- [Cal.com signup](https://app.cal.com/signup)
- [Nylas signup](https://dashboard.nylas.com/register)
- [Cronofy trial](https://app.cronofy.com/sign_up)

Do not run two public schedulers against the same availability as an automatic failover. Simultaneous bookings can race before either service writes the Google Calendar event. A standby provider is safe only when its public links are disabled until cutover.
<!--/ai-->

