n,k = map(int,input().split(' '))
count = 0
for i in range(n):
    data = int(input())
    if data == k:
        count += 1
print(count)
