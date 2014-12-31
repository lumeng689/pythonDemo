#!/usr/bin/env python

"this is a test module"

import sys
import os

__author__ = 'lumeng'

myString = "hello world"

print myString

print "%s is number %d!" % ("Python",1)


print >> sys.stderr, 'Fatal error!'
print sys.platform
print sys.version

print os.linesep

# user = raw_input("Enter your name:")
# print user

print int("123")

print 3//2
print 3**2

print 3 < 4 and 2 > 1

import decimal

print 1.1
print decimal.Decimal('1.1')

pystr = 'python'
iscool = 'iscool'

print pystr[0]

print pystr[-5:-1]

print pystr * 2

aList = [1,2,3,4,5]
print len(aList)

aDict = {"host":"earth"}
aDict['port'] = 80

print aDict

for key in aDict:
    print key , aDict[key]

x = 3
if x < .0:
    print "x must be greater than 0"
elif x < 1:
    print "x < 1"
else:
    print "xxxxx"

counter = 0
while counter < 5:
    print "loop :%d" % counter
    counter += 1

for item in ['a','b','c','d']:
    print item

for item in ['a','b','c','d']:
    print item,

foo = 'abcdefg'

for i,ch in enumerate(foo):
    print ch,'%d' % i

squared = [x**2 for x in range(4)]

for i in squared:
    print i,


squared = [x**2 for x in range(16) if not x % 2]

for i in squared:
    print i,

fobj = open('d:/test/mdm.sql', 'r')

# for eachline in fobj:
    # print eachline

fobj.close()

def addMe2Me(x):
    print 'apply + operation to argument'
    return (x + x)

print addMe2Me(3)


class FooClass(object):
    """my very first class"""
    version = 0.1

    def __init__(self, nm='John Doe'):
        self.name = nm
        print 'Create a class instance'

    def showName(self):
        print 'Your name is',self.name
        print 'My name is ',self.__class__.__name__

    def showVersion(self):
        print self.version


foo1 = FooClass()
foo1.showName()
foo1.showVersion()


# if import __name__ is module name,if run,__name__ is '__main__'
print __name__

print type(12)

a = 'ab'
b = a
print a is b

b = 'a' + 'b'
print a is b

s='abcdefg'

#inverse
print s[::-1]

