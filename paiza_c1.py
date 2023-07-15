# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num = int(input())
sum1 = 0
for i in range(num):
    ans1 = 0
    data = input()
    array1 = data.split(' ')
    A = int(array1[0])
    B = int(array1[1])
    if A == B:
        ans1 = A * B
    else:
        ans1 = A + B
    sum1 += ans1
print(sum1)
