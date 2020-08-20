from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']
SERVICE_ACCOUNT_FILE = 'service_account.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = googleapiclient.discovery.build('classroom', 'v1', credentials=credentials)
results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])

if not courses:
        print('No courses found.')
else:
        print('Courses:')
for course in courses:
        print(course['name'])
