# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
import re

s = input()
s_1 = re.sub(r'\-{3,}',"/",s)
array1 = s_1.split("/")
for str1 in array1:
    print(str1)