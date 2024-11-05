# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

def recursive(x,d,e,k):
    if k == 1:
        return x
    elif k % 2 == 0:
        return recursive(x,d,e,k-1) + e
    elif k % 2 == 1:
        return recursive(x,d,e,k-1) + d


x,d,e,k = map(int,input().split(' '))


ans = recursive(x,d,e,k)
print(ans)
