#!/usr/bin/env python3
# coding:utf-8
import sys
if len(sys.argv) < 3:
    print("Wrong Parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)
f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2], 'w')
f2.write(s)
f2.close()

# 这个程序想干嘛？完全摸不着头脑