N = int(input())

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

sorted_A = sorted(A)
print(sorted_A[N - 1], sorted_A[0])
