# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import sys
sys.setrecursionlimit(10**6)

def recursive(x,d1,d2,n):
    if n == 1:
        return x
    elif n % 2 == 1:
        return recursive(x,d1,d2,n-1) + d1
    elif n % 2 == 0:
        return recursive(x,d1,d2,n-1) + d2


x,d1,d2 = map(int,input().split(' '))
count = int(input())
for i in range(count):
    n = int(input())
    ans = recursive(x,d1,d2,n)
    print(ans)
