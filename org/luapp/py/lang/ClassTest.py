#!/usr/bin/env python
# coding:utf-8


class OldStyleClass:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NewStyleClass(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Programmer(object):

    hobby = 'Play Compute'

    def __new__(cls, *args, **kwargs):
        print 'call __new__ method'
        print args
        return super(Programmer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age, weight):
        print 'call __init__ method'
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_age(self):
        return self._age

    def self_introduction(self):
        print 'My Name is %s, I am %s years old' %(self.name, self._age)

class BackendProgrammer(Programmer):

    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print 'My Name is %s, My favorite language is %s' % (self.name, self.language)

if __name__ == '__main__':
    programmer = Programmer('ZhangSan', 25, 70)

    print dir(programmer)
    print programmer.__dict__
    print programmer.get_weight()
    print Programmer.get_hobby()
    print programmer.get_age
    print programmer._Programmer__weight
    print programmer.self_introduction()

    backendProgrammer = BackendProgrammer('LiSi', 26, 75, 'Java')
    backendProgrammer.self_introduction()

    print isinstance(backendProgrammer, Programmer)
    print isinstance(backendProgrammer, BackendProgrammer)