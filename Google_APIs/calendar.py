from google.oauth2 import service_account

service = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/calendar.readonly',
            'https://www.googleapis.com/auth/calendar',
            'https://www.googleapis.com/auth/calendar.events.readonly'
            'https://www.googleapis.com/auth/calendar.events'],
    subject='nikolay.vaklinov@infinitelambda.com')

calendar = service.calendars().get(calendarId='primary').execute()

print(calendar['summary'])