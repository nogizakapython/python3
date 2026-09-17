# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,a,b = map(int,input().split())
signal_array = list(input())
a_array = list(input())
b_array = list(input())

a_count = 0
b_count = 0
#print(signal_array)
for i in range(n):
    s = signal_array[i]
    a_l = len(a_array)
    b_l = len(b_array)
    if a_l > 0:
        a_data = a_array[0]
        if a_data == s:
            a_array.pop(0)
        
    if b_l > 0:
        b_data = b_array[0]
        if b_data == s:
            b_array.pop(0)
        

print(str(len(a_array)) + " " + str(len(b_array)))