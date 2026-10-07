# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
a = list(map(int,input().split()))
s = [0] * (n + 1)

for i in range(n):
    s[i+1] = s[i] + a[i]

max_sum = 0
for j in range(0,n - 2):
    data = s[j + 3] - s[j]
    if data > max_sum:
        max_sum = data
print(max_sum)
