n = int(input())
array1 = [int(input()) for _ in range(n)]
p,e = map(int,input().split(' '))
array1.insert(p,e)

for k in array1:
    print(k)

