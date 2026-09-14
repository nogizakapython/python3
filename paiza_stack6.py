# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = []
for i in range(n):
    data = input().split()
    if data[0] == "1":
        array1.append(data[1])
    elif data[0] == "2":
        delete_item = array1.pop(0)
        print(delete_item)
    print((" ").join(array1))    
