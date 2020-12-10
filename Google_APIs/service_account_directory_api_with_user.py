from google.oauth2 import service_account
import googleapiclient.discovery
import random
import json

il_super_admin_list = ['nikolay.vaklinov@infinitelambda.com', 'marton.hubay@infinitelambda.com', 'nas.radev@infinitelambda.com', 'peter.tar@infinitelambda.com']
super_admin = 'rams@inniveinc.com'
super_admin2 = random.choice(il_super_admin_list)
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/admin.directory.customer',
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
'https://www.googleapis.com/auth/cloud-platform'],
    subject=super_admin2)
service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)
results = service.resources().calendars().list(customer='my_customer').execute()

print(json.dumps(results, indent=2))