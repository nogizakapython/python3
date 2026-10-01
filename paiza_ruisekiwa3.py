# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
p,q = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * 11
for i in range(10):
    s[i + 1] = s[i] + a[i]
print(s[q + 1] - s[p ])