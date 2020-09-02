from http.client import HTTPResponse
from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

proxy_handler = ProxyHandler({
    'http': '103.99.177.32:8080'
})
opener = build_opener(proxy_handler)

try:
    resp: HTTPResponse = opener.open("http://baidu.com")
    headers = resp.getheaders()
    print(headers)
except URLError as e:
    print(e.reason)
