# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math


num = int(input())
inputdata = input()
array1 = list(map(int,inputdata.split(' ')))
avg = sum(array1) / num
avg1 = avg * 10
amari = avg1 % 10
if amari > 0:
    avg1 += 10
avg = int(avg1 / 10)
print(math.ceil(avg))
