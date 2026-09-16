# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n,c = map(int,input().split())
array1 = list(map(int,input().split(" ")))
result_array = sorted(array1,reverse=True)
count = 0
for num in array1:
    if num >= c:
        count += 1
if count >= int(n /2) + 1:
    print("0")
else:    
    i = int(len(array1) / 2)
    ans = c - result_array[i]
    print(ans)