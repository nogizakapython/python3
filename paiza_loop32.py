N = int(input())
a = list(map(int, input().split()))

ans = 10000
for i in range(N):
    ans = min(ans, a[i] + (i + 1))

print(ans)
