__author__ = 'lumeng'

myString = "hello world"

print myString

print "%s is number %d!" % ("Python",1)

import sys
print >> sys.stderr, 'Fatal error!'

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