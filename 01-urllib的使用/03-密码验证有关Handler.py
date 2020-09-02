from http.client import HTTPResponse
from urllib.request import HTTPPasswordMgrWithPriorAuth, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
passwd = 'passwd'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithPriorAuth()
p.add_password(None, url, user=username, passwd=passwd)

auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    resp: HTTPResponse = opener.open(url)
    html = resp.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
