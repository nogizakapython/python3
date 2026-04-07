# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N = int(input())
min_length = 101
max_length = 0
array1 = input().split(" ")
for i in range(N):
    count = len(array1[i])
    if count < min_length:
        min_length = count
    if count > max_length:
        max_length = count
print(max_length - min_length)