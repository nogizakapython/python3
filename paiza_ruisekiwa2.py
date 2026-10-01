# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = list(map(int,input().split()))
ans = sum(array1) - (array1[0] + array1[1] + array1[8] + array1[9])
print(ans)