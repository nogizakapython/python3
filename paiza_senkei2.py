# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
array1 = [ int(x) for x in input().split(' ')]
k = int(input())
count = 0
for i in range(n):
    data = array1[i]
    if data == k:
        count = i + 1
        break
if count > 0:
    print(count)
else:    
    print(0)