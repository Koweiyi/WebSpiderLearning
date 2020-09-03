# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/03
@file: 猫眼top100爬取.py
@function:
@modify:
"""
from urllib import request, parse
import time
import random
import re

from fake_useragent import UserAgent


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # 1.请求
    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        req = request.Request(url=url, headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode()

        return html

    # 2.解析
    def parse_html(self, html):
        pattern = re.compile(
            r'<p class="name"><a .*? title="(.*?)".*?>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>',
            re.S)
        r_list = pattern.findall(html)
        # print(r_list)
        for r in r_list:
            print("电影名称：", r[0].strip())
            print(r[1].strip())
            print(r[2].strip())
            print('*' * 50)

        # return r_list

    # 3.保存html到本地
    def save_html(self, filename, html):
        with open(filename, 'w', encoding='utf-8')as f:
            f.write(html)

    # 4.入口函数
    def run(self):
        for page in range(1, 10 + 1):
            pn = (page - 1) * 10
            url = self.url.format(pn)
            html = self.get_html(url)
            filename = '猫眼电影' + '-第%s页.html' % str(page)
            self.save_html(filename, html)
            self.parse_html(html)
            print('第%d页抓取成功' % page)
            # 每抓取一页要随机休眠2-3秒
            time.sleep(random.uniform(2, 3))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
