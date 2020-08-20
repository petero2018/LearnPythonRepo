from google.oauth2 import service_account
import googleapiclient.discovery

SCOPES = ['https://www.googleapis.com/auth/classroom.announcements',
'https://www.googleapis.com/auth/classroom.courses',
'https://www.googleapis.com/auth/classroom.coursework.me',
'https://www.googleapis.com/auth/classroom.coursework.students',
'https://www.googleapis.com/auth/classroom.guardianlinks.students',
'https://www.googleapis.com/auth/classroom.profile.emails',
'https://www.googleapis.com/auth/classroom.profile.photos',
'https://www.googleapis.com/auth/classroom.push-notifications',
'https://www.googleapis.com/auth/classroom.rosters',
'https://www.googleapis.com/auth/classroom.topics']
SERVICE_ACCOUNT_FILE = 'service_account.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject='nikolay.vaklinov@infinitelambda.com')

service = googleapiclient.discovery.build('classroom', 'v1', credentials=credentials)
payload = {'name': 'XLTM21 - Traditional', 'section': 'T01', 'descriptionHeading': 'FUNCT MATH 10', 'description': 'xxxxx', 'room': '19', 'ownerId': 'iris.wesley@edfi.org', 'courseState': 'PROVISIONED'}
course_response = service.courses().create(body=payload).execute()

print(course_response)