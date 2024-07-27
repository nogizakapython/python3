N, Q = map(int, input().split())

S = {}
for i in range(N):
    s = input()
    if s not in S:
        S[s] = i + 1

for _ in range(Q):
    t = input()
    if t in S:
        print(S[t])
    else:
        print(-1)
