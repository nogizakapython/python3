# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s = input()
l = len(s)
b = s[0]
e = s[l-1]
flag1 = 0


for i in range(len(array1)):
    t = array1[i]

    if t == b:
        flag1 = 1
    if t == e:
        flag1 = 2
    if flag1 >= 1:
        print(t)
    if flag1 == 2:
        break
