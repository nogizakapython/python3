values = input().split()
N = int(values[0])
K = int(values[1])

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

for a in A:
    if a >= K:
        print(a)
