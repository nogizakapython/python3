# coding: utf-8
# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
#
# 練習用問題セット（レベルアップ問題集）
# https://paiza.jp/works/mondai/cd_rank_input_problems/problem_index?language_uid=python3
# ==========================================================
# ここからコードを書き始めてください
array1 = [int(x) for x in input().split(' ')]
array2 = [int(x) for x in input().split(' ')]
array3 = [int(x) for x in input().split(' ')]
array4 = [int(x) for x in input().split(' ')]

for i in array1:
    print(i + 1)

for j in array2:
    print(j + 1)

for k in array3:
    print(k + 1)

for l in array4:
    print(l + 1)
