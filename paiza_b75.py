# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N,K = map(int,input().split(' '))
array1 = []
for i in range(N):
    data1 = input()
    array1.append(data1)

for j in range(K):
    ans = ""
    data2 = input()
    a,b = data2.split(' ')
    a = int(a)
    data3 = array1[a-1]
    w_array = data3.split(' ')
    w_array[0] = b
    M = len(w_array)
    ans = ""
    for k in range(M):
        if k == M-1:
            ans = ans + w_array[k]
        else:
            ans = ans + w_array[k] + " "
    array1[a-1] = ans

for str1 in array1:
    print(str1)
