# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,k = map(int,input().split())
array1 = list(map(int,input().split()))
s = [0] * (n-k + 2)

for i in range(n-k+1):
    d_sum = 0
    for j in range(i,i+k):  
        d_sum += array1[j]
    s[i + 1] = d_sum
  
print(max(s))