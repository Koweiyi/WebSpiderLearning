# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/05
@file: 05-csv格式数据的写入.py
@function:
@modify:
"""
import csv

# 将列表写入文件
with open('data_1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'id'])
    writer.writerow(['bob', 21, 13423])
    writer.writerow(['kitty', 18, 45322])

# 将字典写入文件
with open('data_2.csv', 'w', encoding='utf8') as f:
    fieldnames = ['name', 'age', 'id']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': "张三", 'age': 21, 'id': 23242})
