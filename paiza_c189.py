# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,k = map(int,input().split())
ans = 0


if k == 1:
    ans = int(n / k)
elif k > 1:    
    if n % 2 == 0 and k % 2 == 0:
        ans = 0
    elif n % 2 != 0 and k % 2 == 0:
        ans = 1

    elif n % 2 == 0 and k % 2 != 0:
        ans = 0
    
    elif n % 2 != 0 and k % 2 != 0:
        ans = 1

print(ans)