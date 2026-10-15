# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

s = "bwwbwbbwbwbb"
n = len(s)

a = [0] * (n)
b = [0] * (n+1)

for i in range(n):
    d = 0
    ch = s[i]
    if ch == "b":
        d = 1 
    a[i] = d 
    
for j in range(n):
    b[j + 1] = b[j] + a[j]

# print(a)
print(b[8] - b[2])