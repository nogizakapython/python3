# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

str1 = input()

ans = re.search('ID-[0-9]+',str1).start()
print(ans)
