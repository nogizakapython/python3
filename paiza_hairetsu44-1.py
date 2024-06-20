N = int(input())

S = [0] * N
values = input().split()
for i in range(N):
    S[i] = values[i]

sorted_S = sorted(S)

for s in sorted_S:
    print(s)
