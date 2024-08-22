n,q = map(int,input().split(' '))
array1 = [int(input()) for _ in range(n)]
for i in range(q):
    #count = 0
    data = int(input())
    if data in array1:
        print("YES")
    else:
        print("NO")
