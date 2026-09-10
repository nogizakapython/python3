# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
#
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,m = map(int,input().split(' '))
array1 = input().split(' ')
p = len(array1)
count = 0
for i in range(p-1):
    str1 = array1[i]
    str2 = array1[i+1]
    ans1 = str1[-n:]
    ans2 = str2[:n]
    if ans1 == ans2:
        count += 1

if count == m - 1:
    print("YES")
else:
    print("NO")
