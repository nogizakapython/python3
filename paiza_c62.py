# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
m,l = map(int,input().split(' '))
count = 0
for i in range(m):
    data = int(input())
    if data <= l:
        count += 1
print(count)
