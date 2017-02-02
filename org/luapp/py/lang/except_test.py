#!/usr/bin/env python
# coding:utf-8

try:
    a
except NameError, e:
    print 'catch error', e

try:
    undef
except:
    print 'catch an exception1'

try:
    if undef:
        print 'undef'
    else:
        print 'come here'
except:
    print 'catch an exception2'

try:
    aaa
except IOError, e:
    print '1111'
except ValueError, e:
    print 'aaaaaa'
except:
    print 33333
finally:
    print 'qqqqqqqq'

try :
    raise TypeError, 'aaaa'
except Exception as e:
    print e
    print '6666'


class CustomError(Exception):
    def __init__(self, info):
        Exception.__init__(self)
        self.errorInfo = info
        print id(self)

    def __str__(self):
        return 'CustomError: %s' % self.errorInfo

try:
    raise CustomError('test CustomError')
except CustomError as e:
    print e
    print id(e)

print '1111'