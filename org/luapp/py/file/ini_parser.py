#!/usr/bin/env python
# coding:utf-8

import ConfigParser

cfg = ConfigParser.ConfigParser()

cfg.read('./conf.txt')

for se in cfg.sections():
    print se
    print cfg.items(se)

print cfg.getint('study', 'base')
