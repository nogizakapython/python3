n,l = map(int,input().split(' '))

for i in range(n):
    data = int(input())
    if l > data:
        l += int(data/2)
    elif l < data:
        l = int(l/2)



print(l)
