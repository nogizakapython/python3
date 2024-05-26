b,t,n = map(int,input().split())
array1 = list(map(int,input().split()))
for i in range(n):
    s = array1[i]
    if s == b:
        array1[i] = t
    print(array1[i])
