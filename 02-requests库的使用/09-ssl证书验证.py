import requests

resp = requests.get('http://118.25.12.189/')
print(resp.status_code)
print(resp.text)