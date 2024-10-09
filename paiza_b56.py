# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,p = map(float,input().split(' '))
n = int(n)
a_sum = 0.0
s_n = 0.0
a_n = 0.0
ans_n = 0
for i in range(n):
    data = float(input())
    a_sum += data

s_n = a_sum / p
a_n = a_sum % p

if a_n > 0:
    s_n += 1

#print(s_n)
ans_n = int(s_n)

print(ans_n)
