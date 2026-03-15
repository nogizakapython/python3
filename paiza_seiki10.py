# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

s = input()
num = re.search('CVE-[0-9]{4}-[0-9]+',s).start()
print(num)
