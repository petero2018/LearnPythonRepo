from google.oauth2 import service_account
import googleapiclient.discovery
import json


credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly', 'https://www.googleapis.com/auth/admin.reports.usage.readonly'],
    subject='nikolay.vaklinov@infinitelambda.com')

service = googleapiclient.discovery.build('admin', 'reports_v1', credentials=credentials)
results = service.userUsageReport().get(
    userKey='all', date='2020-08-01',
    parameters='gmail:num_emails_received,gmail:num_emails_sent,gmail:timestamp_last_access,gmail:timestamp_last_interaction',
    maxResults=1
    ).execute()

print('-'*200)
print(json.dumps(results, indent=2))