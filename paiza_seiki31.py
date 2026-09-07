# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
import re


s = input()
ans1 = re.search(r'(?:n|st|vac)ation([0-9a-zA-Z]+)',s).group(0)
ans2 = re.search(r'(?:n|st|vac)ation([0-9a-zA-Z]+)',s).group(1)
print(ans1)
print(ans2)
