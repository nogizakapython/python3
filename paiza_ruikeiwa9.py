# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
a = [1,5,9,7,5,3,2,5,8,4]
b = [0] * 10
s = [0] * 11

for i in range(len(a)):
    data = 0
    d = a[i]
    if d % 2 == 0:
       data = 1 
    b[i] = data

for j in range(len(b)):
    s[j + 1] = s[j] + b[j]


print(s[8] - s[2])