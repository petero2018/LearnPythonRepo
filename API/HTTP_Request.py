from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import requests
import time
from os import environ

DEFAULT_TIMEOUT = 5


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def api_request(**kwargs):

    url = kwargs.get('url', None)
    auth = kwargs.get('auth', None)
    headers = kwargs.get('headers', None)
    qparams = kwargs.get('qparams', None)

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[408, 429, 500, 501, 502, 503, 504, 507, 509, 510, 511, 598, 599],
        method_whitelist=["HEAD", "GET", "OPTIONS"]
    )

    http = requests.Session()
    adapter = TimeoutHTTPAdapter(timeout=2.5, max_retries=retry_strategy)
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    t0 = time.time()
    try:
        response = http.get(url=url, auth=auth, headers=headers, params=qparams)
        response.encoding = response.apparent_encoding
        status_code = response.status_code
        file_format = kwargs.get('file_format', 'csv' if 'csv' in response.headers.get('Content-Type') else 'json')
        assert file_format in ['csv', 'json']
    except Exception as e:
        print('Failed to request data from API')
        print(f'Error message from server:\n{str(e)}')
    else:
        if not status_code >= 200 and status_code <= 299:
            raise Exception
        print(f'API request to {response.url} with\nformat: {file_format}\nstatus code: {status_code}\nparams: {qparams}\nwas successful!')

        if file_format == 'json':
            return response.json()

        if file_format == 'csv':
            return response.text
    finally:
        t1 = time.time()
        print('Took', t1 - t0, 'seconds')


base_url = 'https://api.adjust.com/kpis/v1/'
app_token = environ.get('ADJUST_API_TOKEN')
user_token = environ.get('ADJUST_USER_TOKEN')
file_format = 'csv'
url = f'{base_url}{app_token}.{file_format}'
header = {'Authorization': f'Token token={user_token}'}
qparams = {
            'timezone_id': '172',
            'start_date': '2020-04-01',
            'end_date': '2020-04-01',
            'kpis': 'clicks,impressions,installs,uninstalls,uninstall_cohort,reinstalls,click_conversion_rate,ctr,impression_conversion_rate,reattributions,reattribution_reinstalls,deattributions,sessions',
            'event_kpis': '',
            'attribution_type': 'click',
            'attribution_source': 'dynamic',
            'grouping': 'date,networks,campaigns,adgroups,creatives,countries,os_names',
            'human_readable_kpis': 'true'}

response = api_request(url=url, headers=header, qparams=qparams)

print(response[:100])