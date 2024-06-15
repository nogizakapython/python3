N = int(input())

S = [0] * N
values = input().split()
for i in range(N):
    S[i] = values[i]

for s in S:
    print(s)
