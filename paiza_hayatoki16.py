# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
s = input()
zero_array = ["C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "S", "T", "U", "V", "W", "X", "Y", "Z"]
one_array = [ "A", "D", "O", "P", "Q", "R"]
two_array = ["B"]
if s in zero_array:
    print(0)
elif s in one_array:
    print(1)
elif s in two_array:
    print(2)