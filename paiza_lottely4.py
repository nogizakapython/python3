# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
b_number = int(input())
before_ad = b_number - 1
after_ad = b_number + 1
ans = ""
n = int(input())
for i in range(n):
    d = int(input())

if before_ad >= 100000 and before_ad <= 199999:
    ans = ans + str(before_ad) + " "

if after_ad >= 100000 and after_ad <= 199999:
    ans = ans + str(after_ad)    
    
print(ans)