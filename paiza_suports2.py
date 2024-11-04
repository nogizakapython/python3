# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
work_hour = int(input())
if work_hour > 6 and work_hour <= 8:
    print("45 min")
elif work_hour > 8:
    print("60 min")
else:
    print("no break")
