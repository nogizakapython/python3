# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math
data = input()
array1 = data.split(' ')
n = int(array1[0])
a = int(array1[1])
b = int(array1[2])
ans = math.floor((b / n)*100)
print(ans)
