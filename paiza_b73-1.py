# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = []

num = int(input())
a.append(0)
a.append(1)
a.append(1)

for j in range(3,41):
    a.append(a[j-1] + a[j-2])

for i in range(num):
    n = int(input())
    print(a[n])
