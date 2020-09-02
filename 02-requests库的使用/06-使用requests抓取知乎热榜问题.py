import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41'
}

resp = requests.get('https://www.zhihu.com/hot', headers=headers)
pattern = re.compile(r'class="css-dk79m8">(.*?)</h1>', re.S)
questions = re.findall(pattern, resp.text)
with open('questions.txt', 'a', encoding='utf-8') as f:
    for question in questions:
        f.write(question)
        f.write('\n')
