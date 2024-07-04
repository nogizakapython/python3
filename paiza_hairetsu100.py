n,k = map(int,input().split(' '))
array1 = []
count = 0
elem = 1
for i in range(n):
    data = int(input())
    if data == k:
        print(elem)
        count += 1
        break
    elem += 1
if count == 0:      
    print(-1)