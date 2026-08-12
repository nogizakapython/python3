# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
N = int(input())
is_prime = [0] * (N + 1)
is_prime[0] = 1
is_prime[1] = 1


for i in range(2,N+1):
    if is_prime[i] == 0:
        for j in range(i * 2,N+1,i):
            is_prime[j] = 1
            

if is_prime[N] == 0:
    print("YES")
else:
    print("NO")