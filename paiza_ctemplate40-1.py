# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
N = int(input())
M = int(input())
a = []
for i in range(M):
    a.append(input())
print(N + 1)
print(M + 1)
for i in range(M):
    print(a[i])
