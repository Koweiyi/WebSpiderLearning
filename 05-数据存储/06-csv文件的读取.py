# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/05
@file: 06-csv文件的读取.py
@function:
@modify:
"""
import csv
with open('data_2.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)