# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

import random

n = int(input())
for i in range(n):
    s = input()
    l = len(s)
    ans = 0
    for j in range(l):
        ans += l + ord(s[j])
        ans %= 100
    print(ans)
