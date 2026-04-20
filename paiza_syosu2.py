# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = 2
for i in range(n):
    array1 = [int(x) for x in input().split(' ')]
    for data in array1:
        data += 1
        print(data)