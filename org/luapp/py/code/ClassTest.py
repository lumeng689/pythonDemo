#! /usr/bin/python
# coding:utf-8

__author__ = 'lumeng'


class MyData(object):
    pass

# 注意，没有 new 关键字
mathObj = MyData()
mathObj.x = 4
mathObj.y = 5

print mathObj.x + mathObj.y


class AddrBookEntry(object):
    '''address book entry class'''

    # static
    foo = 100

    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for:', self.name

    def updatePhone(self, newPh):
        self.phone = newPh
        print 'Updated phone# for:', self.name

print AddrBookEntry.foo

class EmplAddrBookEntry(AddrBookEntry):
    '''empl address book entry class'''
    def __init__(self, nm, ph, id, em):
        AddrBookEntry.__init__(self, nm, ph)
        self.empId = id
        self.email = em

    def updateEmail(self, newEm):
        self.email = newEm

print dir(EmplAddrBookEntry)

print EmplAddrBookEntry.__dict__
print EmplAddrBookEntry.__module__
print EmplAddrBookEntry.__class__
print EmplAddrBookEntry.__doc__