import requests

url = 'http://httpbin.org/post'
data = {
    'name': '孔维一',
    'age': 21
}

resp = requests.post(url, data=data)
print(type(resp))
print(resp)
print(resp.text)
print(resp.json())
