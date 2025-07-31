# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
h,m = map(float,input().split(' '))
change_m = m / 60
total_h = h + change_m


if total_h > 7 and total_h <= 13:
    print("lunch")
elif total_h > 13 and total_h <= 19:
    print("dinner")
elif total_h <= 7 or total_h  > 19:
    print("breakfast")
