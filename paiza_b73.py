# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return recursive(n-2) + recursive(n-1)


num = int(input())
for i in range(num):
    n = int(input())
    ans = recursive(n)
    print(ans)
