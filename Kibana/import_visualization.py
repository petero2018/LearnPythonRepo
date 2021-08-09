import requests

USERNAME, PASSWORD = 'elastic', 'e03m5Hwo8dZa8QXFcau24764'

files = {
  'file': open('/Users/peterosztodi/PycharmProjects/lab-competitionforclimate/reporting/kibana-objects-old.ndjson', 'rb')
}

headers = {'kbn-xsrf': 'true'}

response = requests.post('https://localhost:5601/api/saved_objects/_import',
                         headers=headers,
                         auth=(USERNAME, PASSWORD),
                         verify=False,
                         files=files
                         )
print(response)