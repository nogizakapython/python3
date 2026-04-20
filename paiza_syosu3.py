# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = 3
for i in range(n):
    array1 = [int(x) for x in input().split(" ")]
    for d in array1:
        print(d + 1)