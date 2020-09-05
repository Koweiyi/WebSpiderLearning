# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/04
@file: 03-从json文件中读取数据.py
@function:
@modify:
"""
import json

with open('data.json', 'r') as f:
    s = f.read()
    data = json.loads(s)
    print(data)
    print(type(data))

print("=" * 50)

data = json.load(open('data.json', 'r'))
print(data)
print(type(data))

