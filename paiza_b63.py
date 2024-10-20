# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
t_blood = input()
n = int(input())
dict1 = {}
for i in range(n):
    key,value = input().split(' ')
    dict1[key] = value

print(dict1[t_blood])
