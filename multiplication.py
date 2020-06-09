#!/usr/bin/env python3
i = 1
print("-" * 60)
while i < 11:
    n = 1
    while n < 11:
        print("{:5d}".format(n * i), end=" ")    #Control the width
        n += 1
    print()
    i += 1
print("-" * 60)