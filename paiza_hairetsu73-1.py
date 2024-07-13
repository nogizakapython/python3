n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = []

for i in range(n):
    if a[i] >= k:
        b.append(a[i])

for i in b:
    print(i)
