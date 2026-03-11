# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
array1 = input().split(" ")
n = int(array1[0])
m = int(array1[1])
data_array = []
for i in range(n):
    data_array.append(0)

for j in range(m):
    w_array = input().split(' ')
    a = int(w_array[0])
    b = int(w_array[1])
    data_array[a-1] = b
    w_count = 0
    elem = len(data_array)
    for k in range(elem):
        data = data_array[k]
        if data == 0:
            w_count += 1 
            
    if w_count == 0:
        break
print(sum(data_array))