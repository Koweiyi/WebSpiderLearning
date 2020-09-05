# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/05
@file: 04-输出json字符串到json文件当中.py
@function:
@modify:
"""
import json

data_en = [
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

data_cn = {
    "姓名": "张三",
    "年龄": 21
}

with open('data_1.json', 'w') as f:
    f.write(json.dumps(data_en))

with open('data_2.json', 'w') as f:
    f.write(json.dumps(data_en, indent=2))

with open('data_3.json', 'w') as f:
    f.write(json.dumps(data_cn, indent=2))

with open('data_4.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data_cn, indent=2, ensure_ascii=False))

json.dump(data_cn, open('data_5.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

