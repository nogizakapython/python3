# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

s = input()
print(re.search(r'database_.{,5}\.db',s).start())
