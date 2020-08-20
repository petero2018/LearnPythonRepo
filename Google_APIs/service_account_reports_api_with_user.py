from google.oauth2 import service_account
import googleapiclient.discovery
import random
import json

il_super_admin_list = ['nikolay.vaklinov@infinitelambda.com', 'marton.hubay@infinitelambda.com', 'nas.radev@infinitelambda.com', 'peter.tar@infinitelambda.com']
super_admin = random.choice(il_super_admin_list)
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.reports.audit.readonly', 'https://www.googleapis.com/auth/admin.reports.usage.readonly'],
    subject=super_admin)
service = googleapiclient.discovery.build('admin', 'reports_v1', credentials=credentials)
results = service.activities().list(userKey='all', applicationName='calendar', maxResults=1).execute()

print(f'With super admin {super_admin}')
print(json.dumps(results, indent=2))