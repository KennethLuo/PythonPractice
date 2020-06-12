#!/usr/bin/env python3
# coding:utf-8

def f(a, data=None):
    if data is None:
        data = []
    data.append(a)
    return data
print(f(1))
