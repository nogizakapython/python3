n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i == k:
        ans += 1

print(ans)
