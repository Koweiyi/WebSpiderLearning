import requests

session = requests.session()
session.get('http://httpbin.org/cookies/set/number/12345')
resp = session.get('http://httpbin.org/cookies')
print(resp.text)
