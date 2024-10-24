# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
dict1 = {}
dict2 = {}
name = input()
p = int(input())
for i in range(p):
    key1,value1 = input().split(' ')
    dict1[key1] = value1
q = int(input())
for j in range(q):
    key2,value2 = input().split(' ')
    dict2[key2] = value2

ans1 = dict1[name]
ans = dict2[ans1]
print(ans)
