# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
bitmask = 1
ans = 0
num = int(input())
while num >= bitmask:
    if num & bitmask == 1:
       ans += 1
    num //= 2

print(ans)
