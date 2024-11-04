# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n = int(input())
dict1 = {}
list1 = []
for i in range(n):
    key,value = input().split(' ')
    dict1[key] = value

for number in dict1.keys():
    list1.append(int(number))

list1.sort()

for num in list1:
    print(str(num) + " " + dict1[str(num)] )
