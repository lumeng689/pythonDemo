__author__ = 'lumeng'

import re

m = re.match('foo','foo')

if m is not None:
    print(m.group())

m = re.search('foo','seafood')
if m is not None:
    print(m.group())

m = re.match('(a)(b)','ab')

if m is not None:
    print(m.group())
    print(m.groups())
    print(m.group(1))
    print(m.group(2))

print(re.findall('car','carry the barcardi to the car'))

print (re.split(':','str1:str2:str3'))