# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
N = int(input())
array1 = []

if N == 1:
    print("NO")
else:
    for i in range(2,int(N ** 0.5) + 1):
        if N % i == 0:
            array1.append(i)

    array_elements = len(array1)

    if array_elements == 2:
        print("YES")
    else:
        print("NO")