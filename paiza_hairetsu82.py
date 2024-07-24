# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

n,q = map(int,input().split(" "))
array1 = [i+1 for i in range(n)]
for j in range(q):
    data = input()
    swap_res = re.match('swap',data)
    resize_res = re.match('resize',data)
    if swap_res:
        w_array1 = data.split(' ')
        A = int(w_array1[1]) - 1
        B = int(w_array1[2]) - 1
        tmp = array1[A]
        array1[A] = array1[B]
        array1[B] = tmp

    elif resize_res:
        w_array2 = data.split(' ')
        C = int(w_array2[1])
        length1 = len(array1)
        if C < length1:
            array1 = array1[:C]
    else:
        array1.reverse()


for number in array1:
    print(number)
