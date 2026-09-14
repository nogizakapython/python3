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
    p = data[0]
    if p == "1":
        array1.append(data[1])
    elif p == "2":
        array1.pop(0)
    ans = (" ").join(array1)
    print(ans)
