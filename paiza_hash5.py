# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください

e = 10
array1 = [-1] * e

n = int(input())

for i in range(n):
    d = int(input())
    data = d
    ans = 0
    flag1 = False
    while flag1 == False:
        ans = data % 10
        if array1[ans] == -1:
            array1[ans] = d
            flag1 = True
        else:
            data += 1
            

for num in array1:
    print(num)