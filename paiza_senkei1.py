# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
array1 = list(map(int,input().split(' ')))
t = int(input())
count = 0
for i in range(n):
    data = array1[i]
    if data == t:
        count += 1
print(count)