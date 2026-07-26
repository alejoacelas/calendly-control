# Calendly → Cal.com migration

Migrated on 2026-07-26 through the authenticated Calendly and Cal.com web apps. The exposed Cal.com API key was not used or stored.

## Events

| Event | Duration | Cal.com link | Availability | Booking window | Notice |
| --- | ---: | --- | --- | ---: | ---: |
| Priority 30 minutes | 30 min | https://cal.com/alejoacelas/p30 | Mon–Sat, 08:00–20:00 America/Bogota | 60 calendar days | 90 min |
| AIM Coaching | 50 min | https://cal.com/alejoacelas/aim-coaching | Date overrides below | 3 calendar days | 4 hours |
| vip 30 min | 30 min | https://cal.com/alejoacelas/vip30 | Mon–Sat, 08:00–20:00 America/Bogota | 18 calendar days | 5 hours |
| vip 50 min | 50 min | https://cal.com/alejoacelas/vip50 | Mon–Sat, 08:00–20:00 America/Bogota | 18 calendar days | 5 hours |
| 15 minutes | 15 min | https://cal.com/alejoacelas/15 | Mon, Tue, Fri, 15:00–21:00 America/Bogota | 18 calendar days | 6 hours |
| 30 minutes | 30 min | https://cal.com/alejoacelas/30 | Mon, Tue, Fri, 15:00–21:00 America/Bogota | 18 calendar days | 6 hours |
| 50 minutes | 50 min | https://cal.com/alejoacelas/50-minutes | Mon, Tue, Fri, 15:00–21:00 America/Bogota | 18 calendar days | 6 hours |

All seven events use Google Meet, add bookings to the existing Google Calendar connection, allow guests, and ask the optional multiline question “Please share anything that will help prepare for our meeting.”

## AIM date overrides

The schedule is stored in America/Los_Angeles so the requested travel-time conversions are explicit:

- 2026-08-01, 08:00–12:00 Los Angeles (08:00–12:00 San Francisco)
- 2026-08-08, 05:00–09:00 Los Angeles (08:00–12:00 Boston)
- 2026-08-15, 05:00–09:00 Los Angeles (08:00–12:00 Boston)

There are no recurring weekly AIM hours. The three-day booking window means August 1 will first appear on July 29.

## Method

1. Read all seven active Calendly event types, including the two collapsed event types.
2. Read each event’s duration, meeting location, weekly or date-specific availability, booking horizon, minimum notice, slug, and invitee question.
3. Confirmed Cal.com’s existing Google Calendar and Google Meet connections.
4. Created three reusable Cal.com availability schedules:
   - `Calendly VIP Bogota`
   - `Calendly Short Bogota`
   - `AIM August 2026`
5. Updated the two Cal.com starter events for the 15- and 30-minute links, then duplicated the configured events for the remaining durations and policies.
6. Read every event back from Cal.com and verified the public catalog, durations, slugs, Google Meet location, assigned schedule, booking limits, guest field, and invitee question.

The pre-existing hidden `Secret meeting` event was left unchanged. Nothing was deleted.
