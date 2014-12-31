__author__ = 'lumeng'

import os

lambdaFunc = lambda x:x*2

print(lambdaFunc(100))

print(type(lambdaFunc))
print(lambdaFunc.__name__)

print(type([].append))

class C(object):
    def __init__(self,*args):
        print 'Instantiated with these arguments:\n',args
    def __call__(self, *args, **kwargs):
        print "I'm callable!called with args :\n",args

c = C()

print(callable(c))

c(3)

print(callable(1))

eval_code = compile('100 + 200','','eval')
print(eval(eval_code))

single_code = compile('print "Hello world"','','single')
exec(single_code)

print(os.system('cd'))