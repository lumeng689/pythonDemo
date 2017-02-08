#!/usr/bin/env python
# coding:utf-8

import urllib
import urllib2

URL = 'https://httpbin.org'
URL_IP = URL + '/ip'
URL_GET = URL + '/get'


def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print '>>>> Response Headers:'
    print response.info()
    print '>>>> Response Body:'
    print ''.join([line for line in response.readlines()])


def use_params_urllib2():
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    print 'Request Params:'
    print params
    response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
    print '>>>> Response Headers:'
    print response.info()
    print '>>>> Response Status Code:'
    print response.getcode()
    print '>>>> Response Body:'
    print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
    use_simple_urllib2()

    use_params_urllib2()