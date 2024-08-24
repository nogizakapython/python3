n,m = map(int,input().split(' '))
array1 = {}
for i in range(n):
    k,v=map(str,input().split(' '))
    array1[k] = v
for j in range(m):
    data = input()
    print(array1[data])
