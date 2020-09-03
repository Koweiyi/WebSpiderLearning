# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 03-斗罗大陆.py
@function:
@modify:
"""
import logging
import requests

from lxml import etree
from fake_useragent import UserAgent

BASE_URL = 'https://qxs.la/15173/'
headers = {
    'User-Agent': UserAgent().random
}
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def get_paragraph_url():
    resp = requests.get(BASE_URL, headers=headers)
    html = etree.HTML(resp.text)
    paragraph_urls = html.xpath('/html/body/div[9]/div[position()>3]/a/@href')
    return paragraph_urls


def scrapy_paragraph(paragraph_url):
    paragraph_url = f'https://qxs.la{paragraph_url}'
    resp = requests.get(paragraph_url, headers=headers)
    html = etree.HTML(resp.text)
    lines = html.xpath('//*[@id="content"]/text()[position()>3]')
    title = html.xpath('/html/body/div[3]/h1/text()')[0]
    with open("斗罗大陆.txt", 'a+', encoding='utf-8') as f:
        f.write(title + '\n\n')
        for line in lines:
            f.write('  ')
            f.write(line)
            f.write('\n')
        f.write('\n\n\n\n\n\n')
    logging.info(f'successfully download paragraph {title}')


if __name__ == '__main__':
    pus = get_paragraph_url()
    print(pus)
    for pu in pus:
        scrapy_paragraph(pu)


