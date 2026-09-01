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

for j in range(n):
    data = array1[j]
    w_array = data.split(',')
    c = int(w_array[0])
    d = int(w_array[1])
    for k in range(j+1,n):
        dat = array1[k]
        x_array = dat.split(",")
        e = int(x_array[0])
        f = int(x_array[1])
        l = abs(e-c) + abs(f - d)
        array2.append(l)

t = int(input())
for s in array2:
    if s <= t:
        ans += 1
 
print(ans)