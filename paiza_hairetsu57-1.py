n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i > ans:
        ans = i

print(ans)
