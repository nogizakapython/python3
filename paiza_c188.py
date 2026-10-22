# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

from decimal import Decimal, ROUND_DOWN

n = int(input())
s = input()
hit = 0
ans = 0.0

for i in range(n):
    c = s[i]
    if c == "1":
        hit += 1


ans = Decimal(hit / n) * 100

print(ans.quantize(Decimal('0.1'), rounding=ROUND_DOWN))