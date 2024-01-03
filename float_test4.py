# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num = int(input())
for i in range(0,num):
    data1 = input()
    array1 = data1.split(' ')
    N = float(array1[0])
    M = int(array1[1])
    ans = "{:.{}f}".format(N,M)
    print(ans)
