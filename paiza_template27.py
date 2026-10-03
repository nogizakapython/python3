# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = []
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
array1.append(a1)
array1.append(a2)
# print(array1)
for i in range(len(array1)):
    for j in range(len(array1[i])):
        data = int(array1[i][j])
        print(data + 1)
# print("XXXXXX")
