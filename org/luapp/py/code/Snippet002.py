#! /usr/bin/python
# coding:utf-8

__author__ = 'lumeng'

import copy
from string import Template

# string template
s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(howmany=3, lang='c++')

foo, bar = 'hello', 'world'

print zip(foo, bar)

hi = '''hi
there
'''

print hi

s = 'abc'
print id(s)
s += 'def'
print id(s)

print u'你好'

aList = ['1', '2', '3', '4']
#aList = List('1', '2', '3', '4)
aList.append(5)
print aList

aList[2] = '3.1'
del aList[3]
print aList

print aList * 2

bList = [i * 2 for i in aList]
print bList

print dir(bList)

aTuple = (1, 2, 3)
print aTuple

dict1 = {}
dict2 = {'name': 'earth', 'port': 80}

print dict2

for key in dict2.keys():
    print key

print dict2.values()

# deep copy
dict3 = copy.deepcopy(dict2)
print dict3

# mutable set
s = set('cheeseshop')
print s
# immutable set
t = frozenset('bookshop')
print t

s = '''
dn: uid=user,ou=${ou},dc=maxcrc,dc=com
objectClass: posixAccount
objectClass: top
objectClass: inetOrgPerson
gidNumber: 0
givenName: first
sn: sec
displayName: dis
uid: user
homeDirectory: home
telephoneNumber: 15011111111
mail: aa@bb.com
cn: dis
uidNumber: 28723
'''

t = Template(s)



print t.substitute(ou='aaaa')
