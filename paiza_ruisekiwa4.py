# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,x,y = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * (n + 1)



for j in range(n):
    s[j + 1] = s[j] + a[j]
print(s[y+1] - s[x])
