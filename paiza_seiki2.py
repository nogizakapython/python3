# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

msg1 = input()
num = re.search(r'\\\(\^ \. \^\)/', msg1).start()
print(num)
