# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

s = input()
a = re.search(r'clang-?format',s).start()
print(a)
