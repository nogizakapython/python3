N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

exist = False
for a in A:
    if a == K:
        exist = True
        break

print("YES" if exist else "NO")
