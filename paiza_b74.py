# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return recursive(n-1) + recursive(n-2)

num = int(input())
ans = recursive(num)
print(ans)
