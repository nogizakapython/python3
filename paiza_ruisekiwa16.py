# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,x,y = map(int,input().split())
s = input()
a = [0] * (n)
b = [0] * (n+1)

for i in range(n):
    d = s[i]
    if d == "b":
        a[i] = 1 

for j in range(n):
    b[j + 1] = b[j] + a[j]

print(b[y] - b[x-1])