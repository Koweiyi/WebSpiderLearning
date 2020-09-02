from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    resp = urlopen('http://cuiqingcai.com/index.html')
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(e.reason)
else:
    print("Request successfully")
