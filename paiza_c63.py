# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,m = map(int,input().split(' '))
array1 = []
for i in range(n):
    input_name = input()
    array1.append(input_name)
print(array1[m%n - 1])
