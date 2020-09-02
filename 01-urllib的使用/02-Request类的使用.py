from http.client import HTTPResponse
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41',
    'Host': 'httpbin.org'
}
dict_ = {
    'word': 'hello'
}

data = bytes(parse.urlencode(dict_), encoding='utf-8')

req = request.Request(url=url, data=data, headers=headers, method='POST')
response: HTTPResponse = request.urlopen(req)

print(response.read().decode('utf-8'))
