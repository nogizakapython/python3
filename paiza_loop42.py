n, k = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(k):
        if a[i][j] > ans:
            ans = a[i][j]

print(ans)
