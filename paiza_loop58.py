n,m,c = map(int,input().split())
array1 = input().split()
array1.insert(m-1,c)
for i in array1:
    print(i)
