# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
data = input()
array1 = data.split(' ')

count = 0
for i in range(2,n):
    b = int(array1[i-2])
    c = int(array1[i-1])
    d = int(array1[i])
    if b == 1 and c == 1 and d == 2:
        count += 1

print(count)     