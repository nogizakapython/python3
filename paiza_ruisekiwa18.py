# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
a = []
s = [[0] * 6 for _ in range(6)]
for i in range(5):
    b = list(map(int,input().split()))
    a.append(b)

for j in range(5):
    for k in range(5):
        s[j + 1][k + 1] = s[j + 1][k] + s[j][k + 1] - s[j][k] + a[j][k]


print(s[4][4] - s[4][1] - s[1][4] + s[1][1])
