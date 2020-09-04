# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 03-爬取斗罗大陆小说.py
@function:
@modify:
"""
import time
import random
import logging
import requests

from lxml import etree
from fake_useragent import UserAgent

BASE_URL = 'https://qxs.la/15173/'
headers = {
    'User-Agent': UserAgent().random,
    'Referer': BASE_URL
}
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def get_paragraph_url():
    resp = requests.get(BASE_URL, headers=headers)
    html = etree.HTML(resp.text)
    paragraph_urls = html.xpath('/html/body/div[9]/div[position()<775 and position()>3]/a/@href')
    return paragraph_urls


def scrapy_paragraph(paragraph_url, file):
    paragraph_url = f'https://qxs.la{paragraph_url}'
    resp = requests.get(paragraph_url, headers=headers)
    html = etree.HTML(resp.text)
    lines = html.xpath('//*[@id="content"]/text()[position()>3]')
    title = html.xpath('/html/body/div[3]/h1/text()')[0]
    file.write(title + '\n\n')
    for line in lines:
        file.write('  ' + line + '\n')
    file.write('\n\n\n\n\n\n')
    logging.info(f'successfully download paragraph {title}')
    time.sleep(random.random())


if __name__ == '__main__':
    pus = get_paragraph_url()
    with open("斗罗大陆.txt", 'a+', encoding='utf-8') as f:
        for pu in pus:
            scrapy_paragraph(pu, f)
