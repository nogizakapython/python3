# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ
import math
array1 = list(map(int,input().split(' ')))
array2 = input().split(' ')
total = sum(array1)
#print(total)
d_total = 0
leng1 = len(array1)
for i in range(0,leng1):
    data1 = array1[i]
    flag = array2[i]
    if flag == "o":
        d_total += data1
#print(d_total)
print(math.floor(d_total / total * 100))
