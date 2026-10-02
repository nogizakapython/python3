# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = [1,5,9,7,5,3,2,5,8,4]

n = len(array1)

s = [0] * (n+1)

max_value = 0

for i in range(n):
    s[i+1] = s[i] + array1[i]

for j in range(n-3):
    value = s[j+3] - s[j]
    if value > max_value:
        max_value = value
print(max_value)
