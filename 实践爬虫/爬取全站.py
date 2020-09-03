import os
import time
import requests
from pyquery import PyQuery as pq
import logging
from requests import HTTPError, ConnectionError
from fake_useragent import UserAgent

BASE_URL = 'https://www.mzitu.com'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def User_Agent(page):
    """
    :param page:
    :return:
    """

    header = {"User-Agent": UserAgent().random,
              'Referer': f'https://www.mzitu.com/page/{page}/'}
    return header


def scrape_page(url, header):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url, headers=header)
        return response.text
    except TimeoutError as a:
        logging.error(f"Error time is Out:{a}")
    except HTTPError as c:
        logging.error(f"Error HTTPError: {c}")
    except ConnectionError as d:
        logging.error(f"Error ConnectionError: {d}")


def scrape_index(page, header):
    index_url = f"{BASE_URL}/page/{page}/"
    return scrape_page(index_url, header)


def parse_index(html):
    doc = pq(html)
    links = doc('#pins > li > span:nth-child(2) > a')
    for link in links.items():
        detail_url = link.attr('href')
        logging.info('Got detail_url %s', detail_url)
        yield detail_url


def scrape_detail(url, header):
    return scrape_page(url, header)


def parse_detail_index(html):
    doc = pq(html)
    picture_max = doc('body > div.main > div.content > div.pagenavi > a:nth-child(7) > span').text()
    title = doc('.main .content .main-title').text()
    return int(picture_max), title


def scrape_detail_page(detail_url, page, header):
    picture_url = f"{detail_url}/{page}"
    html = scrape_page(picture_url, header)
    doc = pq(html)
    pic = doc('body > div.main > div.content > div.main-image > p > a > img')
    try:
        src = pic.attr('src')
        if src:
            logging.info(f'The Picture_url {src}...', )
            return src
    except Exception as e:
        print(e)


def scrape_picture(url, page, header, title):
    response = requests.get(url, headers=header).content
    file_name = title + '-' + str(page) + '.jpg'
    item = title + '/' + file_name
    logging.info(f'Successfully acquired: {file_name}')
    with open(item, 'wb+')as f:
        f.write(response)


def main(page):
    header = User_Agent(page)
    index_html = scrape_index(page, header)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url, header)
        picture_max, title = parse_detail_index(detail_html)
        print(title)
        if not os.path.exists(title):
            os.mkdir(title)
        for a in range(1, picture_max + 1):
            picture_url = scrape_detail_page(detail_url, a, header)
            scrape_picture(picture_url, a, header, title)


if __name__ == '__main__':
    for page_ in range(2, 3):
        main(page_)
    time.sleep(1)
