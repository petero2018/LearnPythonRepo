from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
import json

credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly', 'https://www.googleapis.com/auth/admin.reports.usage.readonly'],
    subject='nikolay.vaklinov@infinitelambda.com`')

collector = []
check_email = 'nas@infinitelambda.com'
delta = datetime.timedelta(days=7)
my_date = datetime.datetime.now() - delta
startTime = my_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + "Z"
endTime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + "Z"

service = googleapiclient.discovery.build('admin', 'reports_v1', credentials=credentials)
request = service.activities().list(userKey='all', applicationName='calendar', maxResults=1000, startTime=startTime, endTime=endTime)
result = request.execute()

while request:

    items = result.get('items')
    for item in items:
        if item.get('actor').get('email') == check_email:
            time_str = item.get('id').get('time')
            #time = datetime.datetime.fromisoformat(time_str.replace('Z', ''))
            events = item.get('events')
            for event in events:
                notification_type = event.get('name')
                calendar_parameters = event.get('parameters')
                #if notification_type == 'create_event':
                collector.append({'time': time_str, 'event': event})
                    #for param in calendar_parameters:
                        #target_calendar_id = event.get('target_calendar_id')
                        #if target_calendar_id != check_email:
                            #print(event)

    request = service.activities().list_next(previous_request=request, previous_response=result)
    if request:
        result = request.execute()

print(json.dumps(collector, indent=2))
