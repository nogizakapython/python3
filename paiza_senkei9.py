# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = list(map(int,input().split(' ')))
l = len(array1)
ans_array = []
for i in range(l):
    num = array1[i]
    if num % 2 == 1:
        ans_array.append(i+1)
print(max(ans_array))
