n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    ans += i

print(ans)
