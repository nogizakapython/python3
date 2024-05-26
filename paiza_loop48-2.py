n = int(input())
a = [int(i) for i in input().split()]
b = [[None] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        b[i][j] = a[i] * a[j]

for i in range(n):
    for j in range(n):
        if j == n - 1:
            print(b[i][j])
        else:
            print(b[i][j], end=" ")
