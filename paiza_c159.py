# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,k = map(int,input().split(' '))
array1 = list(map(int,input().split(' ')))
array2 = list(map(int,input().split(' ')))
count = 0
for i in range(k):
    for j in range(n):
        target_n = array2[i]
        correct_n = array1[j]
        if target_n == correct_n:
            print(i+1)
            count += 1

if count == 0:
    print(-1)
