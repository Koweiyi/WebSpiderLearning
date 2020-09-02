import urllib.request
import urllib.error

try:
    resp = urllib.request.urlopen("http://cuiqingcai.com/index.html")
except urllib.error.URLError as e:
    print(e.reason)
