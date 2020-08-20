from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = [
        'https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly',
        'https://www.googleapis.com/auth/admin.directory.device.chromeos'
        ]
SERVICE_ACCOUNT_FILE = 'service_account.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject='nikolay.vaklinov@infinitelambda.com')

service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

request = service.chromeosdevices().list(customerId='my_customer',
                                         #projection='FULL', orderBy='status', sortOrder='ASCENDING',
                                                   maxResults=1000
                                                   )
result = request.execute()
print(result)