# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
num = int(input())
array1 = []
calc = num
count = 0
while calc > 0:
    amari = calc % 2
    array1.append(amari)
    calc //= 2

reversed(array1)

for i in list(array1):
    if i == 1:
        count += 1
print(count)
