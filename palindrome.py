#!/usr/bin/env python3
#coding=utf-8
s = input("Please enter a string: ")
z = s[::-1] # 把输入的字符串s进行倒序处理形成新的字符串z
if s == z:
    print("The string is palindrome")
else:
    print("The string is not a palindrom")

# 切片a[1:2:3] 的意思： 两个冒号分开三个参数：
#
# 第一个参数表示从哪里开始切（包含参数位置），默认从头开始；
#
# 第二个参数表示哪里结束（不包含参数位置），默认一直到尾巴；
#
# （你可以把字符串想象成一个闭环，头和尾都是同一个地方）
#
# 第三个参数表示切片的步长，（表示一刀切多少，正数表示从左往右切，负数表示从右往左切）默认步长包括整个区间。

#O(1)