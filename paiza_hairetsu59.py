n,k = map(int,input().split(' '))
array1 = [int(input()) for _ in range(n)]
count = 0
for i in array1:
    if i == k:
        count += 1

if count > 0:
    print("Yes")
else:
    print("No")
