values = input().split()
N = int(values[0])
K = int(values[1])

S = [0] * N
values = input().split()
for i in range(N):
    S[i] = values[i]

sorted_S = sorted(S)

print(sorted_S[K - 1])
