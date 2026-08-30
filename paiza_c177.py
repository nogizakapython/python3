# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n =int(input())
k,m = map(int,input().split(' '))
array1 = list(map(int,input().split(' ')))
k_count = 0
money_count = 0
for i in range(n):
    num = array1[i]
    if num >= k:
        k_count += 1
    money_count += num
if k_count >= 3 and money_count >= m:
    print("silver")
else:
    print("bronze")
