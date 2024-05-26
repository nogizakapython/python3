b,t,n = map(int,input().split())
array1 = list(map(int,input().split()))
for i in range(n):
    if array1[i] == b:
        array1[i] = t
    print(array1[i])
