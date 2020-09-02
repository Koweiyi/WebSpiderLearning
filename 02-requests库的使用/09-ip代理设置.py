import requests

proxies = {
    'http': '50.233.15.242:8080',
    'https': '102.164.212.54:8080'
}

resp = requests.get('https://baidu.com', proxies=proxies)
print(resp.text)
print(resp.headers)
