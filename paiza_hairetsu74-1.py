n = int(input())
m = list(map(int,input().split()))
ans = 0

for i in range(n):
    a = list(map(int, input().split()))
    score = 0
    for j in range(5):
        score += a[j] * m[j]
    if score > ans:
        ans = score

print(ans)
