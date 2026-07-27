# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
b_number = int(input())
b_second = b_number % 10000
n = int(input())
for i in range(n):
    t_number = int(input())
    t_second = t_number % 10000
    if t_second == b_second:
        print("second")
    else:    
        print("blank")