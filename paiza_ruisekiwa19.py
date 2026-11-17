# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
a,b = map(int,input().split())
array1 = []
t_sum = 0
for i in range(5):
    w_array = list(map(int,input().split()))
    array1.append(w_array)

for i in range(5):
    for j in range(5):
        if i >= a and i <= b and j == 3:
            t_sum += array1[i][j]
print(t_sum)