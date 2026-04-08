# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
array1 = [ int(x) for x in input().split(" ") ]
t = int(input())

for i in range(n):
    data = array1[i]
    if data == t:
        print(i+1)