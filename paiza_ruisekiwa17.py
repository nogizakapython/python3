# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

array1 = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]

b = [[0] * 5 for i in range(5)]


d_sum = 0
for j in range(1,4):
    for k in range(1,4):
        data = array1[j][k]
        d_sum += data


print(d_sum)
