# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
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
    data = input()
    w_array = data.split(" ")
    p = w_array[0]
    ans = ""
    if p == "1":
        d = w_array[1]
        array1.append(d)
        num = len(array1)
        
    elif p == "2":
        num = len(array1)
        print(array1[num - 1])
        array1.pop()
        num = len(array1)
    ans = (" ").join(array1)
    print(ans)