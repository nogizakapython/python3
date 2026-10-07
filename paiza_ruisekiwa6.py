# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = list(map(int,input().split()))
array2 = []

for i in range(len(array1) - 2):
    ans = 0
    ans = array1[i] + array1[i+1] + array1[i+2]
    array2.append(ans)
print(max(array2))
