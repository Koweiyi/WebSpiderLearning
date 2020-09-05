# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/04
@file: 02-读取json格式字符串.py
@function:
@modify:
"""
import json

string = '''
[
    {
        "name": "bob",
        "age": 21,
        "gender": "male"
    },
    {
        "name": "Lily",
        "age": 18,
        "gender": "female"
    }
]
'''
data = json.loads(string)
print(data)
print(type(data))

# 获取内容
print(data[0]['name'])  # bob
print(data[0].get('name'))  # bob

print(data[0].get('birth'))  # None
print(data[0].get('birth', '1999-11-27'))  # 1999-11-27
