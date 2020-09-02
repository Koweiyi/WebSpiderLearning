import re

import requests


def get_one_page(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.83 Mobile Safari/537.36 Edg/85.0.564.41'
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        with open("maoyan.html", 'w', encoding='utf-8') as f:
            f.write(resp.text)
        return resp.text
    else:
        return None


def parse_one_page(html: str):
    # <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
    # .*?name.*?<a.*?>(.*?)</a>.*?<p.*?>(.*?)</p>.*?<p.*?><i.*?>(.*?)<i/><i.*?>(.*?)<i/>
    print(html)
    items = re.findall('<dd>.*?board-index.*?>(.*?)</i>', html, re.S)
    print(items)
    # yield {
    #     'index': items[0],
    #
    # }
    pass


if __name__ == '__main__':
    url_ = 'https://maoyan.com/board/4?offset=10'
    html_ = get_one_page(url_)
    parse_one_page(html_)
