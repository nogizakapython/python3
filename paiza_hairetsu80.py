n,k,f = map(int,input().split(' '))
array1 = []
for i in range(k):
    data1 = int(input())
    array1.append(data1)

#print(array1)

del array1[:f]

#print(array1)

array2 = []
for k in array1:
    if k in array2:
        continue
    else:
        array2.append(k)

for l in array2:
    print(l)
