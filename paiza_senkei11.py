# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
max_value = -101

n = int(input())
array1 = list(map(int,input().split(' ')))
t = int(input())
for num in array1:
    if num <= t and num > max_value:
        max_value = num

print(max_value)
