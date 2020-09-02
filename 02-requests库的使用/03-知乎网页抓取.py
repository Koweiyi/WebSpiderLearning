import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41'
}
url = 'https://www.zhihu.com/explore'

resp = requests.get(url, headers=headers)
pattern = re.compile('explore-feed.*?class="question_link".*?>(.*?)</a>', re.S)
titles = re.findall(pattern, resp.text)
for title in titles:
    print(title.replace("\n", ''))

# https://www.zhihu.com/node/ExploreAnswerListV2?params=%7B%22offset%22%3A30%2C%22type%22%3A%22day%22%7D

# https://www.zhihu.com/node/ExploreAnswerListV2?params=%7B%22offset%22%3A5%2C%22type%22%3A%22day%22%7D


