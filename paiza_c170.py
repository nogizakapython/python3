# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = list(map(int,input().split(' ')))
base_num = array1[1]
array2 = list(map(int,input().split(' ')))
point = 0
t_point = base_num
for data in list(array2):
    point += int(data / 100)

if point >= t_point:
    print(0)
else:
    print((t_point - point) * 100 )
