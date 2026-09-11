# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = []
n = int(input())
for i in range(n):
    x = input()
    if x == "2":
        array1.pop(-1)
    else:
        w_array = x.split(" ")
        array1.append(int(w_array[1]))
    

    l = len(array1)
    ans = ""
    for i in range(l):
        if i == l- 1:
            ans = ans + str(array1[i])
        else:
            ans = ans + str(array1[i]) + " "

    print(ans)        
    