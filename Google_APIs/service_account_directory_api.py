from google.oauth2 import service_account
import googleapiclient.discovery
import json

SCOPES = [
'https://www.googleapis.com/auth/admin.directory.customer',
'https://www.googleapis.com/auth/admin.directory.customer.readonly',
'https://www.googleapis.com/auth/admin.directory.device.chromeos',
'https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly',
'https://www.googleapis.com/auth/admin.directory.device.mobile',
'https://www.googleapis.com/auth/admin.directory.device.mobile.action',
'https://www.googleapis.com/auth/admin.directory.device.mobile.readonly',
'https://www.googleapis.com/auth/admin.directory.domain',
'https://www.googleapis.com/auth/admin.directory.domain.readonly',
'https://www.googleapis.com/auth/admin.directory.group',
'https://www.googleapis.com/auth/admin.directory.group.member',
'https://www.googleapis.com/auth/admin.directory.group.member.readonly',
'https://www.googleapis.com/auth/admin.directory.group.readonly',
'https://www.googleapis.com/auth/admin.directory.notifications',
'https://www.googleapis.com/auth/admin.directory.orgunit',
'https://www.googleapis.com/auth/admin.directory.orgunit.readonly',
'https://www.googleapis.com/auth/admin.directory.resource.calendar',
'https://www.googleapis.com/auth/admin.directory.resource.calendar.readonly',
'https://www.googleapis.com/auth/admin.directory.rolemanagement',
'https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly',
'https://www.googleapis.com/auth/admin.directory.user',
'https://www.googleapis.com/auth/admin.directory.user.alias',
'https://www.googleapis.com/auth/admin.directory.user.alias.readonly',
'https://www.googleapis.com/auth/admin.directory.user.readonly',
'https://www.googleapis.com/auth/admin.directory.user.security',
'https://www.googleapis.com/auth/admin.directory.userschema',
'https://www.googleapis.com/auth/admin.directory.userschema.readonly',
'https://www.googleapis.com/auth/cloud-platform'
                    ]
SERVICE_ACCOUNT_FILE = 'service_account_SFUSD.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject='innive360@sfusd.edu') # 'nikolay.vaklinov@infinitelambda.com' 'rams@inniveinc.com'

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

for _ in range(100):
    request1 = service.mobiledevices().list(customerId='my_customer', maxResults=1000, projection='FULL', orderBy='status', sortOrder='ASCENDING')
    results1 = request1.execute()
    results2 = service.mobiledevices().list_next(previous_request=request1, previous_response=results1)

    print('-'*100, 'results1', '-'*100)
    print(json.dumps(results1, indent=2))
    print('')
    print('-'*100, 'results2', '-'*100)
    print(json.dumps(results2, indent=2))
    print('')
    print(_ + 1)