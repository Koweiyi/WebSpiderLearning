import requests

resp = requests.get('http://www.baidu.com')
print(type(resp))
print(resp.status_code)
print(type(resp.text))
print(resp.text)
print(resp.cookies)