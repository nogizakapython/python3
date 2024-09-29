# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
ans = 0
for i in range(n,n+10,1):
    if i >= 10:
        ans = i % 10
    else:
        ans = i
    print(ans)
