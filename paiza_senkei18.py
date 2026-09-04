# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = []
for i in range(n):
    data = input()
    array1.append(data)
x_s,x_t = map(int,input().split(" "))
y_s,y_t = map(int,input().split(" "))
correct_count = 0

for d in array1:
    x,y = map(int,d.split(" "))
    
    check_count = 0
    if x >= x_s and x <= x_t:
        check_count += 1
    if y >= y_s and y <= y_t:
        check_count += 1 
    if check_count == 2:
       correct_count += 1 
print(correct_count)