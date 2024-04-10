N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = max(ans, a[i] + (i + 1))

print(ans)
