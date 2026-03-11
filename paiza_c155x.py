# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
s = input()
n = int(input())
array1 = []
for i in range(n):
    r = input()
    array1.append(r)

for word in array1:
    if s in word:
        print("Yes")
    else:
        print("No")
