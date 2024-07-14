n, k, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i >= k:
        ans += 1
ans -= m
if ans < 0:
    ans = 0

print(ans)
