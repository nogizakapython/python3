# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
N = int(input())
fermat = 1
a = 2

one_count = 0
if N == 1:
    print("NO")
elif N == 2:
    print("YES")
else:    
    for i in range(1,N):
        feamat =  a ** i
        amari = feamat % N
        if amari == 1 and i == N - 1:
            print("YES")
        elif i == N - 1 and amari != 1:
            print("NO")
