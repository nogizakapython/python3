# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,x,y = map(int,input().split())
for i in range(n):
    a,b = map(int,input().split())
    if (a >= x and b >= x) and a + b >= y:
        print("Yes")
    else:
        print("No")