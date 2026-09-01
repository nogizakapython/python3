n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())

xn, yn = points[-1]
answer = 0

for xi, yi in points:
    if abs(xi - xn) + abs(yi - yn) <= k:
        answer += 1

print(answer)