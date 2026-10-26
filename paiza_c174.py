# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())

for i in range(n):
    s = input()
    t = input()
    
    s_array = sorted(s,reverse = True)
    t_array = sorted(t,reverse = True)
    
    fin_s = "".join(sorted(s_array,reverse = True))
    fin_t = "".join(sorted(t_array,reverse = True))
    
    if fin_s == fin_t:
        print("Yes")
    else:
        print("No")
    