N = int(input())

avg = 0
A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])
    avg += A[i]

avg /= N
for a in A:
    if a >= avg:
        print(a)
