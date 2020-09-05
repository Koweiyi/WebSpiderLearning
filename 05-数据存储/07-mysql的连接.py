# -*- coding:utf-8 _*-
"""
@version: 1.0.0
author: 孔维一
@time: 2020/09/05
@file: 07-mysql的连接.py
@function:
@modify:
"""
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='274210Kwy')
cursor = db.cursor()
cursor.execute('select version()')
data = cursor.fetchone()
print(f'Database version is :{data}')
cursor.execute('create database spiders default character set utf8')
db.close()
