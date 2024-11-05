# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def recursive(x,d,n):
    if n == 1:
        return x
    else:
        return recursive(x,d,n-1) + d

x,d,n = map(int,input().split(' '))
ans = recursive(x,d,n)
print(ans)
