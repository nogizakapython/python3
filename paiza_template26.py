# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
array1 = list(map(int,input().split()))
num2 = int(input())
array3 = list(map(int,input().split()))
for num1 in array1:
    print(num1 + 1)
print(num2 + 1)

for num3 in array3:
    print(num3 + 1)
