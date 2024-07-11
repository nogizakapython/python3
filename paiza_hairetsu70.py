m,n = map(int,input().split(' '))
array1 = []
array2 = []
for i in range(m):
    data = int(input())
    array1.append(data)

for k in range(n):
    if k < m:
        array2.append(array1[k])
    else:
        array2.append(0)

for l in array2:
    print(l)
