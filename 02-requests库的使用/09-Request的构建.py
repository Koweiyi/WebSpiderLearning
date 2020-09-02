import requests
from requests import Request, session

url = 'http://httpbin.org/post'
data = {
    'name': 'koweiyi'
}

proxies = {
    'http': '179.95.235.138:8080'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41',
    'proxies': '179.95.235.138:8080'
}

s = session()
request = Request('POST', url, data=data, headers=headers)
prepared = s.prepare_request(request)

resp = s.send(prepared)

print(resp.text)

