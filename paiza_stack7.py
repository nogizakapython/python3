# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = []
array2 = []
for i in range(n):
    data = input().split()
    if data[0] == "1":
        if data[1] == "1":
            array1.append(data[2])
        elif data[1] == "2":
            array2.append(data[2])
    elif data[0] == "2":
        if data[1] == "1":
            print(array1.pop(0))
        else:
            print(array2.pop(0))
    elif data[0] == "3":
        print(str(len(array1)) + " " + str(len(array2)))