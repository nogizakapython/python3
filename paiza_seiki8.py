# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import re

s = input()
ans = re.search(f'congratulations!*',s).start()
print(ans)
