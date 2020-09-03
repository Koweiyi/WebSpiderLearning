# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 02-爬取全站.py
@function:
@modify:
"""
import os
import logging
import requests

from pyquery import PyQuery as pq
from fake_useragent import UserAgent

BASE_URL = 'https://www.mzitu.com'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def user_agent(page):
    return {
        'User-Agent': UserAgent().random,
        'Referer': f'http://www.mzitu.com/page/{page}/'
    }


def scrapy_page(url, header):
    try:
        resp = requests.get(url, headers=header)
        return resp.text
    except TimeoutError as e:
        logging.error(f'Error Timeout: {e}')
    except requests.HTTPError as e:
        logging.error(f'HTTPError: {e}')
    except requests.ConnectionError as e:
        logging.error(f'ConnectionError: {e}')


def scrapy_index(page, header):
    url = f'{BASE_URL}/page/{page}/'
    return scrapy_page(url, header)


def parse_index(index_html):
    doc = pq(index_html)
    links = doc('#pins > li > a')
    for link in links:
        detail_url = link.attrib['href']
        yield detail_url


def parse_detail_html(detail_html):
    doc = pq(detail_html)
    pic_max = doc('body > div.main > div.content > div.pagenavi > a:nth-child(7) > span').text()
    title = doc('body > div.main > div.content > h2').text()
    return int(pic_max), title


def parse_pic_html(pic_html, index, title, header):
    doc = pq(pic_html)
    pic_url = doc('body > div.main > div.content > div.main-image > p > a > img').attr('src')
    filename = title + '/' + title + '-' + str(index) + '.jpg'
    pic = requests.get(pic_url, header).content
    logging.info(f'Successfully acquired: {filename}')
    with open(filename, 'wb+') as f:
        f.write(pic)


def scrapy(page):
    header = user_agent(page)
    index_html = scrapy_index(page, header)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrapy_page(detail_url, header)
        pic_max, title = parse_detail_html(detail_html)
        print(title)
        if not os.path.exists(title):
            os.mkdir(title)
        for i in range(1, pic_max + 1):
            pic_html_url = detail_url + '/' + str(i)
            pic_html = scrapy_page(pic_html_url, header)
            parse_pic_html(pic_html, i, title, header)


if __name__ == '__main__':
    for page_ in range(3, 255):
        scrapy(page_)
