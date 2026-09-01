# ==========================================================
# 【Python3】標準入力の書き方に困ったらこちら！
# 
# 「入力される値」の取得方法一覧（Python）
# https://paiza.jp/pages/works/cheatsheet/stdin_python
# ==========================================================
# ここからコードを書き始めてください
n = int(input())
array1 = []
array2 = []
ans = 0
for i in range(n):
    a,b = map(int,input().split(" "))
    array1.append(str(a) + "," + str(b))

dat = array1[n-1]
x_i,y_i = map(int,dat.split(","))
d = 0

for data in array1:
    x_x,y_y = map(int,data.split(','))
    d = abs(x_x - x_i) + abs(y_y - y_i)
    array2.append(d)

t = int(input())

for distance in array2:
    if distance <= t:
        ans += 1
        
print(ans)        