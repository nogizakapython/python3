# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = list(map(int,input().split()))
b = [0] * (len(array1))
s = [0] * (len(b) + 1)

for i in range(len(array1)):
    d = 0
    data = array1[i]
    if data % 2 == 0:
        d = 1 
    b[i] = d

for j in range(len(b)):
    s[j+1] = s[j] + b[j]
print(s[8] - s[2])