# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
A,B = map(int,input().split(' '))
ans = ""
if B - A > 0:
    ans = "+" + str(B - A)
else:
    ans = B - A
print(ans)
