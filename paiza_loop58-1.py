values = input().split()
N = int(values[0])
M = int(values[1])
K = int(values[2])

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

A.insert(M - 1, K)

for a in A:
    print(a)
