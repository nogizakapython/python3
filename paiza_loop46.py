n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

ans = -10000
for i in range(n):
    for j in range(k):
        ab = a[i] * b[j]
        if ab > ans:
            ans = ab

print(ans)
