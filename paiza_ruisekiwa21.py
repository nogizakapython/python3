# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
a,b,c,d = map(int,input().split())
array1 = []
t_sum = 0
for i in range(n):
    array2 = list(map(int,input().split()))
    array1.append(array2)
    
for j in range(n):
    for k in range(n):
        if j >= a and j <= c:
            if k >= b and k <= d:
                e = array1[j][k]
                t_sum += e
        
        
print(t_sum)