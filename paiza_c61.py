# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = []
O_count = 0
X_count = 0
for i in range(5):
    data = list(input())
    array1.append(data)



for h in range(5):
    a_data = ""
    for k in range(5):
        a_data += array1[h][k]
    if a_data == "OOOOO":
        O_count += 1
    elif a_data == "XXXXX":
        X_count += 1


for k in range(5):
    b_data = ""
    for l in range(5):
        b_data += array1[l][k]
    if b_data == "OOOOO":
        O_count += 1
    elif b_data == "XXXXX":
        X_count += 1

c_data = ""
for a in range(5):
    c_data += array1[a][a]
if c_data == "OOOOO":
    O_count += 1
elif c_data == "XXXXX":
    X_count += 1

d_data = ""
for b in range(5):
    d_data += array1[b][4-b]
if d_data == "OOOOO":
    O_count += 1
elif d_data == "XXXXX":
    X_count += 1

if O_count > X_count:
    print("O")
elif O_count < X_count:
    print("X")
else:
    print("D")
