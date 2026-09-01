# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
import re

s = input()
ans = re.search("G[A-Z]??C",s).start()
ansb = re.search("G[A-Z]??C",s).group()
print(ans)
print(ansb)