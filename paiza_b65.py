# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
dict1 = {}
dict2 = {}

n = int(input())
for i in range(n):
    key1,value1 = input().split(' ')
    dict1[key1] = value1
x = int(input())
for j in range(x):
    key2,value2 = input().split(' ')
    dict2[key2] = value2

leng1 = len(dict1)
for name,blood in dict1.items():
    ans = dict2[blood]
    print(name + " " + ans)
