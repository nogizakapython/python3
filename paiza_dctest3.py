# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
# a, b, cのいずれか2つが整数
a, op, b, e, c = input().split()
if a.isdigit():
    a = int(a) + 1
if b.isdigit():
    b = int(b) + 1
if c.isdigit():
    c = int(c) + 1
print(a)
print(op)
print(b)
print(e)
print(c)