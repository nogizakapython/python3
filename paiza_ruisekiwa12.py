# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,x,y = map(int,input().split())
array1 = list(map(int,input().split()))
b = [0] * (n)
s = [0] * (n+1)

for i in range(n):
    d = 0
    data = array1[i]
    if data % 2 == 0:
        d = 1 
    b[i] = d    

for j in range(n):
    s[j + 1] = s[j] + b[j]

print(s[y + 1] - s[x])