# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
a,b = map(int,input().split(' '))
array1 = [0] * a

for i in range(b):
    data1,data2 = map(int,input().split(' '))
    array1[data1-1] = data2
    zero_count = 0
    for d in array1:
        if d == 0:
            zero_count += 1
    if zero_count == 0:
        print(sum(array1))
        break
