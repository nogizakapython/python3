N = int(input())

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

for a in A:
    if a >= 5:
        print(a)
