n = int(input())
a = [int(input()) for _ in range(n)]
b = [None] * n

for i in range(n):
    b[i] = a[n - i - 1]

for i in b:
    print(i)
