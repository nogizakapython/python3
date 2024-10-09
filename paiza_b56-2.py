v = input().split()
N = int(v[0])
K = float(v[1])

total = 0
for _ in range(N):
    x = float(input())
    total += round(x * 10)

ans = int(total / round(K * 10))
if total % round(K * 10) != 0:
    ans += 1
print(ans)
