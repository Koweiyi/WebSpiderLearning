import requests

url = 'https://www.zhihu.com/people/xiu-xing-sheng'
headers = {
    'Cookie': 'd_c0="ADClFdUkPw6PTqW_4vHFYqCGEpZQhYcydPM=|1537535682"; _zap=43ae0b24-b243-4f0c-aa08-89f31e1845e2; _xsrf=chrdSrIHOaPEtLz3kOw43fenI5H3ANHD; _ga=GA1.2.250904670.1582965764; z_c0=Mi4xU1ZUUEF3QUFBQUFBTUtVVjFTUV9EaGNBQUFCaEFsVk43SXFiWHdDZzhUZWdyMHN2VmxtLWo3bi1Kc2VoWVRRUE93|1588477164|fa251eb744c329409f578542ebf5fa690a18e165; tst=h; tshl=; q_c1=cd4323fd653744abbeca856b8d5840df|1598707836000|1537535683000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1598337934,1598707809,1598851475,1598869127; SESSIONID=hsWjuN4XGt3htQUqf4SEj7siJGRUyp7bmsj4YFNMiPl; JOID=W1AQC0JJZ98ByvsXOkhmwaQlXZQnIBmFar-0Lm8OEuFkv6pDRga_n1_L9xc2yqT7dTbkUQODgvBRXa3HWcQa7Y0=; osd=W1AWCkpJZ9kAwvsXPEluwaQjXJwnIB-EYr-0KG4GEuFivqJDRgC-l1_L8RY-yqT9dD7kUQWCivBRW6zPWcQc7IU=; KLBRSID=57358d62405ef24305120316801fd92a|1598871643|1598869126; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1598871643',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41',
    'host': 'www.zhihu.com'
}

resp = requests.get(url, headers=headers)
print(resp.text)

with open('zhihu.html', 'w', encoding='utf-8') as f:
    f.write(resp.text)
