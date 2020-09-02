import requests

params = {
    'name': '孔维一',
    'age': 21
}

resp = requests.get('http://httpbin.org/get', params=params)
print(resp.text)

resp = requests.get('http://httpbin.org/get', params=params)

print(type(resp))
print(resp.json())
print(type(resp.json()))

'''
out:
{
  "args": {
    "age": "21", 
    "name": "\u5b54\u7ef4\u4e00"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.24.0", 
    "X-Amzn-Trace-Id": "Root=1-5f4c886e-05facbb55564ee64a0577044"
  }, 
  "origin": "36.106.253.99", 
  "url": "http://httpbin.org/get?name=\u5b54\u7ef4\u4e00&age=21"
}

<class 'requests.models.Response'>
{'args': {'age': '21', 'name': '孔维一'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id': 
 'Root=1-5f4c886e-835bf083e46826241dd8bc4e'}, 'origin': '36.106.253.99', 
 'url': 'http://httpbin.org/get?name=孔维一&age=21'}
<class 'dict'>

'''