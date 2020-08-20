from google.oauth2 import service_account
import googleapiclient.discovery
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly', 'https://www.googleapis.com/auth/admin.reports.usage.readonly'],
    subject='rams@inniveinc.com') # 'nikolay.vaklinov@infinitelambda.com'
service = googleapiclient.discovery.build('admin', 'reports_v1', credentials=credentials)
results = service.activities().list(userKey='all', applicationName='calendar', maxResults=1000).execute()
items = results.get('items')

for item in items:
    print(item)