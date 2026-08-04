# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
import re


s = input()
if re.search(r'\w{3}-\d{3,4}',s):
    ans = re.search(r'\w{3}-\d{3,4}',s).start()
    print(ans)