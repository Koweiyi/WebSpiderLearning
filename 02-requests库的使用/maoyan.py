import requests
from requests.exceptions import RequestException
from lxml import etree
import json
import random
import time


def get_one_page(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('Requests error!')
        return None


def parse_one_page(html):
    """
    :param html: html.text
    :return: items
    """
    html_xpath = etree.HTML(html)
    items = []
    for each in html_xpath.xpath('//*[@id="app"]/div/div/div[1]/dl/dd'):
        rank = each.xpath('./i/text()')[0]
        title = each.xpath('./a[@href]/@title')[0]
        img_addr = each.xpath('./a[@href]/img[@class="board-img"]/@data-src')[0]
        actors = each.xpath('./div/div/div/p/text()')[0].strip("主演： \n")
        release_time = each.xpath('./div/div/div/p[@class="releasetime"]/text()')[0][5:]

        score_list = each.xpath('./div/div/div[2]/p//i/text()')
        score = str(score_list[0] + score_list[1])
        items.append({
            'rank': rank,
            'title': title,
            'img_addr': img_addr,
            'actors': actors,
            'release time': release_time,
            'score': score
        })
    return items


def write_to_file(content):
    """
    :param content: a dict
    :return:
    """
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main():
    for page in range(0, 100, 10):
        url = 'https://maoyan.com/board/4?offset=' + str(page)
        html = get_one_page(url)
        # print(html)
        items = parse_one_page(html)
        for each in items:
            print(each)
            write_to_file(each)
        time.sleep(random.random())

    return


if __name__ == '__main__':
    main()