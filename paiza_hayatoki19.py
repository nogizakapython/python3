# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
match(n):
    case n if n >= 20 and n <= 15000:
        print("yes")

    case n if n > 15000 and n <= 20000:
        print("not sure")

    case n if n < 20 or n > 20000:
        print("no")
