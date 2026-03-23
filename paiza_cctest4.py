# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
year = int(input())
if year % 100 == 0 and year % 400 == 0:
    print("Leap")
elif year % 100 == 0 and year % 400 != 0:
    print("Common")
elif year % 4 == 0:
    print("Leap")
else:    
    print("Common")