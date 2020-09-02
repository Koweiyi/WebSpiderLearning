import urllib.request
import urllib.parse
import urllib.error
import socket
from http.client import HTTPResponse

response: HTTPResponse = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader("server"))

# urlopen中data参数的使用
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# urlopen中timeout参数的使用
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
