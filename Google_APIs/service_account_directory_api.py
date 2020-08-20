from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly',
                    'https://www.googleapis.com/auth/admin.directory.device.chromeos',
                    'https://www.googleapis.com/auth/admin.directory.device.mobile.readonly',
                    'https://www.googleapis.com/auth/admin.directory.device.mobile',
                    'https://www.googleapis.com/auth/admin.directory.device.mobile.action'
                    ]
SERVICE_ACCOUNT_FILE = 'service_account.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject='rams@inniveinc.com') # 'nikolay.vaklinov@infinitelambda.com'

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

# Call the Admin SDK Directory API
print('Getting the first 10 users in the domain')
# results = service.chromeosdevices().list(customerId='my_customer', maxResults=1000, projection='FULL', orderBy='status', sortOrder='ASCENDING').execute()

# results = service.mobiledevices().list(customerId='my_customer', maxResults=1000, projection='FULL', orderBy='status', sortOrder='ASCENDING').execute()