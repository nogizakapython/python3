# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import math
point = int(input())
kangen_late = int(input())
total_point = 0
for i in range(7):
    total_point += point
    point = math.floor(int(kangen_late / 100 * point))




print(total_point)
