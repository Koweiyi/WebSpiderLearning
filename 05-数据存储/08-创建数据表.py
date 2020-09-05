# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/05
@file: 08-创建数据表.py
@function:
@modify:
"""

import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='274210Kwy',
    db='spiders'
)
cursor = db.cursor()
sql = 'create table if not exists students(id varchar(255) not null, ' \
      'name varchar(255) not null , age int not null ,primary key (id))'

cursor.execute(sql)
db.close()
