# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
N = int(input())
flag = True

if N != 1:
   for i in range(2,int(N /2 ) + 1):
        if N % i == 0:
            flag = False
            break
else:
    flag = False

if flag:
    print("YES")
else:
    print("NO")        
   

    