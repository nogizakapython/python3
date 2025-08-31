# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num = int(input())
array1 = []
for i in range(num):
    data1 = input()
    array1.append(data1)

array1.sort(reverse=True)
for result1 in array1:
    result = result1.split(' ')
    print(result[1])
