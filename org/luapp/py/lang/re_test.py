#!/usr/bin/env python
# coding:utf-8

import re

str1 = 'python 22323'
pa = re.compile(r'(python)', re.I)
ma = pa.match(str1)

print ma.string
print ma.span()
print ma.group()
print ma.groups()