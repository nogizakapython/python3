# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
l = 0
r = 0
for i in range(n):
    w_array = input().split(" ")
    
    p = w_array[0]
    s = w_array[1]
    w = int(w_array[2])
    
    if p == "1":
        if s == "L":
            l +=  w
        elif s == "R":
            r += w
    
    if p == "3":
        if s == "L":
            l -= w
            r += w
        else:
            r -= w
            l += w
    
    if p == "2":
        if s == "L":
            l = l -  w
        else:
            r = r - w 
    if l > r:
        print(">")
    elif l == r:
        print("=")
    elif l < r:
        print("<")
        