#!/usr/bin/env python
# coding:utf-8
import os
import sys
import codecs


def print_file_meta(f):
    print '文件元信息'
    print type(f)
    print 'fileno： %d' % f.fileno()
    print 'file mode： %s' % f.mode
    print 'file encoding： %s' % f.encoding
    print 'file closed： %s' % f.closed
    print '========================='

print '标准输入文件信息 \n'
print_file_meta(sys.stdin)
print '标准输出文件信息 \n'
print_file_meta(sys.stdout)
print '标准错误文件信息 \n'
print_file_meta(sys.stderr)

f1 = open('../code/Snippet001.py')
print_file_meta(f1)
c = f1.read()
print c
f1.close()

f2 = open('./test.txt', 'w')
f2.write('您好11111111中国\n')
f2.write(unicode.encode(u'您好世界\n', 'utf-8'))
f2.close()

f3 = open('./test.txt', 'a')
f3.write('222222\n')
f3.close()

f4 = open('../code/Snippet001.py')
iter_f = iter(f4)
lines = 0
for line in iter_f:
    lines +=1

print '总共有 %d 行' % lines


f5 = open('./test.txt', 'a')
f5.writelines(('1','2','3'))
f5.writelines(['a','b','c'])
f5.flush()
f5.close()

f6 = open('./test.txt', 'r')
print '原始文件指针 %d ' % f6.tell()
word = f6.read(3)
print word
print '读取3个字节后指针 %d' % f6.tell()

f6.seek(0, os.SEEK_SET)
print 'SEEK_SET 后指针位置 %d' % f6.tell()
print f6.read()
f6.seek(-5, os.SEEK_CUR)
print 'SEEK_CUR 后指针位置 %d' % f6.tell()
print f6.read()
f6.close()

f7 = codecs.open('./test.txt', 'a', 'utf-8')
print_file_meta(f7)
f7.write(u'您好世界2\n')
f7.close()

fd = os.open('./test2.txt',os.O_CREAT | os.O_RDWR)
print fd
n = os.write(fd, 'testeset')
print n
print os.lseek(fd, 0, os.SEEK_SET)
os.write(fd, 'aa')
os.close(fd)

print os.access('./test2.txt', os.R_OK)
print os.access('./test2.txt', os.W_OK)
print os.access('./test2.txt', os.X_OK)

print os.listdir('.')

print os.path.exists('./test2.txt')
print os.path.isfile('./test2.txt')