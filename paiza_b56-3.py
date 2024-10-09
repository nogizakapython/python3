import math

N, K = map(float, input().split())

total = 0
for _ in range(int(N)):
    x = float(input())
    total += round(x * 10)

ans = math.ceil(total / round(K * 10))
print(ans)
