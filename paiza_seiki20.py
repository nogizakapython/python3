# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
import re

s = input()
l = len(s)

result = re.search(r'[0-9a-f]{64}',s)

if result:
    print(re.search(r'[0-9a-f]{64}',s).start())
    print(re.search(r'[0-9a-f]{64}',s).group())