# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
match n:
    case n if  n < 30:
        print("quiet")
    case n if n >= 30 and n < 50:
        print("normal")
    case n if n >= 50 and n < 70:
        print("noisy")
    case n if n > 70:
        print("very noisy")
