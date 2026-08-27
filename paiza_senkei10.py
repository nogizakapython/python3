# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = list(map(int,input().split(' ')))
k = int(input())
min_num = 101
for num in array1:
    if num >= k and num < min_num:
        min_num = num

print(min_num)
