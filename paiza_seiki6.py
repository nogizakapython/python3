# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import re

str1 = input()
a = re.search(r'[A-Z]-[0-9][0-9][a-b]',str1).start()
print(a)
