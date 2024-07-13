n,k= map(int,input().split(' '))
array1 = [int(input()) for _ in range(n)]
array2 = []
for i in array1:
    if i >= k and i <= 100:
        array2.append(i)

for j in array2:
    print(j)
