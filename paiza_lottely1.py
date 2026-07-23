# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
b_number = int(input())
second_check = b_number % 10000
third_check = b_number % 1000
n = int(input())
for i in range(n):
    t_number = int(input())
    if t_number == b_number:
        print("first")
    elif abs(t_number - b_number) == 1:
        print("adjacent")
    elif (t_number % 10000) == second_check:
        print("second")
    elif (t_number % 1000) == third_check:
        print("third")
    else:
        print("blank")
