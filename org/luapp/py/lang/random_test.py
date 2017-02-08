#!/usr/bin/env python
# coding:utf-8

import random

if __name__ == '__main__':

    # 生成 0-1的随机数
    print random.random()
    #  生成一个 10-20之间的随机数
    print random.uniform(10, 20)
    #
    print random.randint(10,20)
    # 10到100之间随机数，递增2
    print random.randrange(10, 100, 2)
    print random.choice(['aa','bb', 1, True])
    p = ['aa','bb', 1, True]
    random.shuffle(p)
    print p

    #  随机获取指定片段，原来的数据不受影响
    list = [1,2,3,4,5,6,7,8,9,10]
    slice = random.sample(list, 5)
    print slice
    print list