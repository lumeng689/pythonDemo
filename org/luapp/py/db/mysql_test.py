#!/usr/bin/env python
# coding:utf-8

"""
mac 下安装MySQLdb
1.修改环境变量
    PATH="/usr/local/mysql/bin:${PATH}"
    export PATH
    export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/
    export VERSIONER_PYTHON_PREFER_64_BIT=no
    export VERSIONER_PYTHON_PREFER_32_BIT=yes
2.pip安装
    pip install MySQL-python

3.修改libmysqlclient.18.dylib 链接
sudo install_name_tool -change libmysqlclient.18.dylib \
  /usr/local/mysql/lib/libmysqlclient.18.dylib \
  /Library/Python/2.7/site-packages/_mysql.so
"""
import MySQLdb

conn = MySQLdb.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='cloud1688',
    db='test',
    charset='utf8'
)

cursor = conn.cursor()
print conn
print cursor

sql = 'select * from user'
cursor.execute(sql)
print cursor.rowcount
rs = cursor.fetchone()
print rs
rs = cursor.fetchmany(3)
print rs
rs = cursor.fetchall()
print rs

cursor.close()
conn.close()






