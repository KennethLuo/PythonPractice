#!/usr/bin/env python3
days = int(input("Enter days:"))
months = days // 30
days = days % 30
print("Months = {} Days = {}".format(months, days))

# Or you can use divmod
days = int(input("Enter days:"))
print("Months = {} Days = {}".format(*divmod(days, 30)))
# Divmod(num1,num2) will return a tuple,which includes 2 numbers.
# The first one = num1 // num2
# The second one = num1 % num2
# Use * to separate the tuple and gain two values
