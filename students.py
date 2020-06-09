#!/usr/bin/env python3
n = int(input("Please enter the number of students:"))
data = {}#用来储存数据的字典变量
Subjects = {'Physics', 'Math', 'History'}#科目
for i in range(0, n):
    name = input('Enter the name of the students {}: '.format(i + 1)) # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科分数
    data[name] = marks
for x, y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x,'Failed :-(')
    else:

        print(x,'Pass :-)')