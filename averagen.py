#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < N:
    number = float(input())
    sum = sum + number
    count = count + 1
averagen = sum / count
print("N = {}, Sum = {}".format(N, sum))
print("The averagern of numbers is {:.2f}".format(averagen))
