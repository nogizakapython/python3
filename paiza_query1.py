n,k,q = map(int,input().split(' '))
array1 = []
for i in range(n):
    data = int(input())
    array1.append(data)
array1.insert(k,q)
for j in array1:
    print(j)
