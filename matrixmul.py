#!/usr/bin/env python3
#这个例子里我们计算两个矩阵的 Hadamard 乘积。要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）
n = int(input('Enter the value of n: '))
print('Enter the value for the Matrix A')
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print('Enter the value for the Matrix B')
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print('After matrix multiplication')
print('-' * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print('-' * 7 * n)