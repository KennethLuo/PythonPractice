#!/usr/bin/env python3
# coding=utf-8
def palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':  #关于这句话的解释在下面
    s = input("Enter a string: ")
    if palindrome(s):
        print("Yay a palindrome")
    else:
        print("Oh no, not a palindrome")

# 解释1：
# 由于每个python模块（python文件）都包含内置的变量name
# 当运行模块被执行时:   name等于文件名（包含后缀.py）
# 如果被import到其他模块中，则name等于模块名称（不包含后缀.py),
#                        而“main”等于当前执行文件的名称（包含了后缀.py）
# 所以当模块被直接执行时:         name == 'main'结果为真；
# 而当模块被import到其他模块时:   name == 'main'结果为假，就是不调用对应的方法。
#
# 解释2：
# 如果该python程序是作为一个脚本独立使用,则该python脚本的name属性就会被解释器自动赋予"main"的值
# 说明这个程序是作为顶层主程序发挥作用的。
#
# 而当该程序作为一个模块被import进去的时候
# 则name != “main”
#
# 这句话的作用一般就是可以保证，当程序处于不同地位时，这个脚本也可以进行相应的不同处理，而不用写两个程序，以保证代码的复用
