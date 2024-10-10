n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

for i in range(n):
    if i < n - 1:
        print(b[i] - a[i], end=" ")
    else:
        print(b[i] - a[i])
