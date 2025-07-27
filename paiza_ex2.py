# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
w_array1 = input().split(' ')
array1 = []
for i in w_array1:
    array1.append(int(i))

array2 = sorted(array1)

array2.pop(0)
leng1 = len(array2)
array2.pop(leng1-1)
print(sum(array2))
