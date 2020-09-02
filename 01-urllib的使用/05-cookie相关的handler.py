import http.cookiejar
import urllib.request
from http.client import HTTPResponse
from urllib.error import URLError

# cookie = http.cookiejar.CookieJar()
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

try:
    resp = opener.open('http://www.baidu.com')
    # for item in cookie:
    #     print(item.name + "=" + item.value)
    cookie.save(ignore_discard=True, ignore_expires=True)
except URLError as e:
    print(e.reason)

# 加载cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

try:
    resp: HTTPResponse = opener.open('http://www.baidu.com')
    print(resp.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
