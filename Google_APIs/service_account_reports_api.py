from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
import json

credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly', 'https://www.googleapis.com/auth/admin.reports.usage.readonly'],
    subject='nikolay.vaklinov@infinitelambda.com')

collector = []
check_email_switch = False
check_target_cal_switch = True
origin_cal_check = 'nas@infinitelambda.com' # 'nas@infinitelambda.com' , 'marton.hubay@infinitelambda.com', 'james@infinitelambda.com'
target_cal_check = ['nas@infinitelambda.com']

delta = datetime.timedelta(days=7)
my_date = datetime.datetime.now() - delta
startTime = my_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + "Z"
endTime = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + "Z"

service = googleapiclient.discovery.build('admin', 'reports_v1', credentials=credentials)
request = service.activities().list(userKey='all', applicationName='calendar', maxResults=1000, startTime=startTime, endTime=endTime, eventName='create_event')
result = request.execute()

while request:

    items = result.get('items')
    for item in items:
        #if check_email_switch and item.get('actor').get('email') == origin_cal_check:
        time_str = item.get('id').get('time')
        events = item.get('events')
        for event in events:
            notification_type = event.get('name')
            calendar_parameters = event.get('parameters')
            target_calendar = [i.get('value') for i in calendar_parameters if i.get('name') == 'target_calendar_id'][0]
            if target_calendar in target_cal_check:
                collector.append({'time': time_str, 'event': event})

    request = service.activities().list_next(previous_request=request, previous_response=result)
    if request:
        result = request.execute()

print(json.dumps(collector, indent=2))
