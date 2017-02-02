#!/usr/bin/env python
# coding:utf-8


"""
  1.安装驱动
  pip install pymongo
"""

from distutils.log import warn as printf
from random import randrange as rand
from pymongo import MongoClient, errors


# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client.test

posts = db.posts
posts.insert({'aa': 1})

print db