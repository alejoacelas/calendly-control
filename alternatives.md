# Calendly alternatives

## Recommendation

Use **Cal.com** if API control is non-negotiable. Use **SavvyCal** if the booking experience matters more than API control.

No hosted product I found satisfies every requirement unchanged:

- **SavvyCal** already distinguishes preferred from merely available times and lets recipients overlay their calendars. Its API can read ranked slots and create bookings, but cannot configure most link availability, durations, booking windows, or preferred-time rules.
- **Cal.com** already has recipient calendar overlay, date overrides, booking rules, conferencing, public links, and broad API control. It does not visibly distinguish preferred from acceptable slots.
- **Cal.com with one booking-page change** is the closest complete solution. Its API supplies the slots; a small open-source change can label slots whose timestamps fall inside a preferred schedule.

The decision changes at one threshold:

- If managing availability in a web UI is acceptable, trial SavvyCal. It delivers both requested user-facing features without a build.
- If agents must create and edit event types and availability through an API, trial Cal.com. Do not migrate until its API reproduces the AIM event end to end.

## Requirements

These come from [API.md](API.md) and the desired booking experience:

1. Create, read, and update event types through an API.
2. Create and update weekly and date-specific availability through an API.
3. Set durations, time zones, buffers, minimum notice, and booking horizons.
4. Read available slots and create, reschedule, and cancel bookings.
5. Check connected calendars for conflicts.
6. Add Google Meet or another conferencing link.
7. Publish reusable and one-time booking links.
8. Receive booking webhooks.
9. Mark some available times as preferred without hiding acceptable times.
10. Let recipients compare the offered times with their own calendars.

The score below gives one point per requirement, or half a point for partial support. A high score does not erase a failure on a non-negotiable requirement.

## Comparison

| Option | Coverage | Preferred times | Recipient calendar | API-controlled setup | Cost for one organizer | Work before use |
| --- | ---: | --- | --- | --- | --- | --- |
| **Cal.com, hosted** | **9/10** | No explicit preferred tier | Native overlay | Strong | Free individual plan; verify required API access in a spike | 4–8 hours |
| **Cal.com, modified** | **9.5/10** | Add to booking page | Native overlay | Strong | Hosting estimate: $20–50/month | 3–7 engineering days |
| **SavvyCal** | **8/10** | Native ranked availability | Native overlay | Partial | $12/month, or $10/month billed annually | 2–4 hours |
| **Nylas + a small app** | **9.5/10** | Build exactly | Build with recipient OAuth | Strong | $10/month includes five connected accounts, then $1.50/account/month | 1–3 engineering weeks |
| **Cronofy + a small app** | **9/10** | Build exactly | Build with recipient OAuth | Strong | Quote required | 2–4 engineering weeks |
| **Zencal** | **6/10** | None found | None found | Partial | $28/month for API access | 4–8 hours |

`Yes` means the vendor documents the capability. `Build` means its APIs provide the necessary data but we must implement the product behavior. `Partial` means a material part still requires the vendor UI or custom code.

| Requirement | Cal.com | SavvyCal | Nylas app | Cronofy app | Zencal |
| --- | --- | --- | --- | --- | --- |
| Event-type API control | Yes | Partial | Yes | Build | Partial |
| Availability and date-override API control | Yes | No | Yes | Yes | No |
| Slot lookup and conflict checking | Yes | Yes | Yes | Yes | Yes |
| Booking lifecycle API | Yes | Yes | Yes | Yes | Partial |
| Booking windows, buffers, and time zones | Yes | UI only | Yes | Build | UI only |
| Conferencing and public booking page | Yes | Yes | Yes | Partial | Yes |
| Webhooks | Yes | Yes | Yes | Yes | Yes |
| Explicit preferred-time tier | No | Yes | Build | Build | No |
| Recipient calendar overlay | Yes | Yes | Build | Build | No |
| Low single-user cost and maintenance | Yes | Yes | Partial | No public price | Partial |

The work estimates are mine, not vendor claims. They assume one organizer, Google Calendar and Google Meet, an existing place to deploy a small web app, and no enterprise security review. Supporting Google, Microsoft, and Apple calendars for recipients pushes a custom build toward the high end.

## 1. Cal.com

### What it fulfills

Cal.com is the best replacement base for agent-controlled scheduling.

- Its API creates and updates event types, including duration, schedule, buffers, minimum notice, booking window, conferencing location, and other booking rules. See [create event type](https://cal.com/docs/api-reference/v2/event-types/create-an-event-type) and [update event type](https://cal.com/docs/api-reference/v2/event-types/update-an-event-type).
- Its schedules API accepts weekly availability, time zones, and date overrides. See [create schedule](https://cal.com/docs/api-reference/v2/schedules/create-a-schedule).
- Its slots API returns bookable times by event type and time zone. See [available slots](https://cal.com/docs/api-reference/v2/slots/get-available-time-slots-for-an-event-type).
- It has booking, rescheduling, cancellation, reservation, and webhook endpoints. See [create booking](https://cal.com/docs/api-reference/v2/bookings/create-a-booking), [reschedule booking](https://cal.com/docs/api-reference/v2/bookings/reschedule-a-booking), [reserve slot](https://cal.com/docs/api-reference/v2/slots/reserve-a-slot), and [webhooks](https://cal.com/docs/api-reference/v2/webhooks/create-a-webhook).
- Its current product page says bookers can [overlay their calendars](https://cal.com/) on the booking page.
- The individual hosted plan is [free](https://cal.com/pricing) and includes unlimited event types and calendars. Teams is $12/user/month on annual billing.

### What it misses

Cal.com's “optimized slots” feature fits meetings around conflicts; it does not mark a narrower subset as preferred while leaving the rest acceptable. The API returns available slots but no preference rank. See [optimized slots](https://cal.com/help/event-types/optimized-slots).

### Smallest path to the missing feature

1. Keep two schedules in our database: acceptable and preferred.
2. Ask Cal.com's API for the actually bookable slots.
3. Mark a returned slot preferred when it also falls inside the preferred schedule.
4. Render preferred slots first or with a visible label; keep acceptable slots selectable.
5. Submit the selected slot through Cal.com's booking API.

This is a small data-model and presentation change. The scheduling engine, conflict checks, booking transaction, conferencing, and recipient overlay remain Cal.com's responsibility.

Self-hosting is only worth it if the native booking page must contain this change. Cal.com's core is open source under AGPLv3, which requires publishing network-facing modifications; that matches this workspace's public-by-default rule. See the [Cal.com repository license](https://github.com/calcom/cal.com).

### Risks to prove before migrating

- API version headers differ by endpoint. Pin and test every request rather than using one global version.
- Cal.com's older Platform/Atoms documentation says that plan is closed to new customers. Do not make Atoms a dependency; use the regular v2 API or modify the open-source booking page.
- Confirm that the individual account exposes every required write endpoint. The public docs support API-key authentication, while the pricing page describes “custom APIs” under Teams.

## 2. SavvyCal

### What it fulfills

SavvyCal is the only finished product I found that directly implements both desired booking-page features.

- It can [highlight preferred times](https://docs.savvycal.com/article/95-optimized-availability) automatically by batching meetings or preferring mornings or afternoons, or manually by using a narrower saved schedule inside broader availability.
- A recipient can [overlay their calendar](https://docs.savvycal.com/article/63-introduction-to-savvycal) on the scheduling link.
- Its slots API returns an explicit `rank`; rank 1 is most preferred. See [available slots](https://developers.savvycal.com/api/get-link-slots).
- Its API can list and create scheduling links, read slots, create events, and manage webhooks. See the [API overview](https://developers.savvycal.com/).
- Basic costs [$12 month-to-month or $10/month billed annually](https://savvycal.com/pricing) and includes ranked availability, conferencing, API access, and webhooks.

### What it misses

The API is not a complete control plane. The documented create and update bodies expose only name, private name, description, and single-use versus recurring type. The update schema does not expose durations, availability, date overrides, booking horizons, conferencing, custom fields, or preferred-time rules. See [UpdateLinkRequest](https://developers.savvycal.com/api/schemas/updatelinkrequest).

The API can read a configured link's durations and ranked slots, but those settings must be configured in SavvyCal's UI. That fails the requirement that an agent reproduce work like the AIM event through direct API calls.

### When to choose it

Choose SavvyCal if:

- preferred-time highlighting is the immediate problem;
- occasional UI configuration is acceptable; and
- a two-hour manual trial is more valuable than building.

Do not choose it if API-controlled availability is a hard requirement.

## 3. Nylas

Nylas is the strongest foundation for a custom product without operating a full scheduling engine.

- Scheduler configurations are created and updated through the API and support public pages, duration, open hours, buffers, time zones, and reminders. See [Scheduler](https://developer.nylas.com/docs/v3/scheduler/).
- It supports [date-specific availability](https://developer.nylas.com/docs/v3/scheduler/managing-availability/), including a mode that ignores weekly hours and offers only specified dates.
- It provides availability and booking APIs plus customizable web components. See [availability](https://developer.nylas.com/docs/reference/api/availability/) and [the scheduling component](https://developer.nylas.com/docs/v3/scheduler/using-scheduling-component/).
- The Calendar plan is [$10/month](https://www.nylas.com/pricing/) for five connected accounts, then $1.50 per connected account per month.

Preferred times are straightforward because we own the front end: rank slots after Nylas returns them. Recipient overlay is possible, but the recipient must authorize calendar access. Each authorization may count as a paid connected account, so this can become more expensive than the organizer-only price suggests.

Choose Nylas when the booking page is becoming a product, not merely a personal scheduling link.

## 4. Cronofy

Cronofy supplies the calendar infrastructure needed for a custom solution:

- Its [Availability API](https://docs.cronofy.com/developers/api/scheduling/availability/) finds common times across connected calendars.
- Its [real-time scheduling endpoint](https://docs.cronofy.com/developers/api/scheduling/real-time-scheduling/) creates hosted selection links.
- Its [UI Elements](https://docs.cronofy.com/developers/ui-elements/) provide slot pickers, availability viewers, and calendar connection controls.
- Its Emerging plan includes availability, working-hours management, and UI elements, but [pricing is not public](https://docs.cronofy.com/developers/plans-pricing/).

Cronofy can support preferred ranking and recipient overlay because we would own the logic and presentation. It is a heavier and less price-transparent choice than Nylas for one organizer. Reconsider it if reliability commitments, data residency, or complex multi-person scheduling become primary.

## 5. Zencal

Zencal handles normal scheduling and service sales but does not solve the distinctive requirements.

- Its API calculates schedules and creates meetings. See [scheduling](https://docs.zencal.io/reference/api-reference/scheduling).
- It can update meeting-topic name, description, enabled state, privacy, and metadata. See [meeting topics](https://docs.zencal.io/reference/api-reference/meeting-topics).
- The documented update endpoint does not expose duration, availability, date overrides, booking windows, or preferred ranking.
- I found no official preferred-time or recipient-calendar-overlay feature.
- API access requires the [$28/month Pro plan](https://zencal.io/pricing/).

It offers less API control than Cal.com and less booking-page differentiation than SavvyCal, at a higher single-user price than either.

## Proposed test

Do not migrate yet. Run one reversible Cal.com spike:

1. Create a free individual account and connect the same Google Calendar and Google Meet.
2. Through the API, reproduce AIM Coaching: 50 minutes, the three date overrides in their local time zones, and a three-day booking horizon.
3. Read the event type and slots back, then make and cancel a test booking.
4. Open the public page as a recipient and test calendar overlay.
5. Prototype preferred labels against the slots response without changing the public scheduler.

Stop if any required API write is unavailable on the individual plan. If the API works, estimate the preferred-label change from the prototype rather than committing to a broad rebuild.

If this spike takes more than one day before preferred-time UI work begins, use SavvyCal for a month and learn whether people actually choose highlighted times more often.
