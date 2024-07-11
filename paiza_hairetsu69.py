num = int(input())
array1 = []
for i in range(num):
    data = int(input())
    array1.append(data)

for j in range(1,num):
    p = array1[j]
    for k in range(0,j):
        q = array1[k]
        print(p * q)
