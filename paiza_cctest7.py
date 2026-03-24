# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,a,b,mod = map(int,input().split(' '))
for i in range(n):
    x = int(input())
    print((a * x + b ) % mod)