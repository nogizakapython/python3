values = input().split()
N = int(values[0])
M = int(values[1])
L = int(values[2])

S = [0] * M
values = input().split()
for i in range(M):
    S[i] = values[i]

print(S[N - 1][L - 1])
