# Calendly alternatives research

## Method

Checked official product, pricing, help, and API documentation on 2026-07-26. Compared each option with the capabilities recorded in `API.md` and the two new user-facing requirements:

- distinguish preferred from acceptable available times;
- optionally show the recipient's own calendar conflicts.

Scoring in `alternatives.md` gives one point for full support and half a point for partial support across ten requirements. Custom-build options receive credit for features that their documented APIs make implementable; their time and operating cost are shown separately.

## Findings that determined the recommendation

### Cal.com

- API v2 documents event-type creation and updates, schedules with overrides, available slots, bookings, reservations, rescheduling, and webhooks.
- Its current marketing page and booking documentation describe recipient calendar overlay.
- “Optimized slots” changes slot placement around conflicts. It is not ranked or visibly preferred availability.
- The individual plan is free. The pricing page places “custom APIs” under Teams, so required write access needs an account-level test.
- Platform/Atoms pages contain deprecation notices for new customers. The recommendation does not depend on Atoms.

### SavvyCal

- Native preferred-time highlighting supports automatic and manual modes.
- Native recipient calendar overlay is part of the booking flow.
- Available-slot API responses include a preference `rank`.
- Public link create/update schemas expose only basic link identity fields. Availability, duration, booking-window, and ranking configuration are absent from the documented write API.

### Nylas

- Scheduler configurations cover event details, weekly and date-specific availability, buffers, time zones, availability lookup, bookings, reminders, and customizable UI.
- A custom UI can rank slots and connect a recipient calendar, but recipient OAuth adds friction and potentially per-account cost.

### Cronofy

- Availability, real-time scheduling, and UI Elements provide the primitives for a custom implementation.
- Required Emerging-plan pricing is not published.

### Zencal

- API schedules meetings and updates a small subset of meeting-topic fields.
- No official evidence found for preferred ranking or recipient calendar overlay.

## Primary sources

### Cal.com

- https://cal.com/docs/api-reference/v2/event-types/create-an-event-type
- https://cal.com/docs/api-reference/v2/event-types/update-an-event-type
- https://cal.com/docs/api-reference/v2/schedules/create-a-schedule
- https://cal.com/docs/api-reference/v2/slots/get-available-time-slots-for-an-event-type
- https://cal.com/docs/api-reference/v2/bookings/create-a-booking
- https://cal.com/docs/api-reference/v2/bookings/reschedule-a-booking
- https://cal.com/docs/api-reference/v2/slots/reserve-a-slot
- https://cal.com/docs/api-reference/v2/webhooks/create-a-webhook
- https://cal.com/help/event-types/optimized-slots
- https://cal.com/pricing
- https://cal.com/
- https://github.com/calcom/cal.com

### SavvyCal

- https://docs.savvycal.com/article/95-optimized-availability
- https://docs.savvycal.com/article/63-introduction-to-savvycal
- https://developers.savvycal.com/
- https://developers.savvycal.com/api/get-link-slots
- https://developers.savvycal.com/api/schemas/updatelinkrequest
- https://savvycal.com/pricing

### Nylas

- https://developer.nylas.com/docs/v3/scheduler/
- https://developer.nylas.com/docs/v3/scheduler/managing-availability/
- https://developer.nylas.com/docs/reference/api/availability/
- https://developer.nylas.com/docs/v3/scheduler/using-scheduling-component/
- https://www.nylas.com/pricing/

### Cronofy

- https://docs.cronofy.com/developers/api/scheduling/availability/
- https://docs.cronofy.com/developers/api/scheduling/real-time-scheduling/
- https://docs.cronofy.com/developers/ui-elements/
- https://docs.cronofy.com/developers/plans-pricing/

### Zencal

- https://docs.zencal.io/reference/api-reference/scheduling
- https://docs.zencal.io/reference/api-reference/meeting-topics
- https://zencal.io/pricing/

## Limits

- No paid trials or vendor accounts were created.
- No API calls were made against candidate products.
- Prices are current page prices and can change.
- Work estimates assume one organizer and exclude provider OAuth verification delays.
