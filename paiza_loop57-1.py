values = input().split()
N = int(values[0])
M = int(values[1])

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

del A[M - 1]

for a in A:
    print(a)
