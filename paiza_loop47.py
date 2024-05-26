array1 = []
n,k = map(int,input().split(' '))
for i in range(n):
    data1 = list(map(int,input().split(' ')))
    array1.append(data1)


for a in range(k):
    for b in range(n):
        if b == n-1:
            print(array1[b][a])
        else:
            print(array1[b][a],end=' ')
