# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,s = map(int,input().split(' '))
array1 = []
for i in range(n):
    data = int(input())
    array1.append(data)
total = sum(array1)
if total > s:
    print("NG")
else:
    print("OK")
