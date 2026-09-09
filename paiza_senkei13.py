# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = []
for i in range(n):
    data=input()
    array1.append(data)
t = int(input())
for d in array1:
    A,B=d.split(' ')
    B = int(B)
    if B >= t:
        print(A)
