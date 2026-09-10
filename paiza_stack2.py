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
    data = input()
    if data != "2":
        a,b = map(int,data.split())
        array1.append(b)

print(len(array1))
for j in array1:
    print(j)