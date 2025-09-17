N, M = map(int, input().split(" "))
ANS = 0
for _ in range(N):
    A = int(input())
    if A <= M:
        ANS += 1

print(ANS)
