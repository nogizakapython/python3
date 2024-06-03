values = input().split()
N = int(values[0])
M = int(values[1])

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

B = [0] * M
values = input().split()
for i in range(M):
    B[i] = int(values[i])

ans = A + B
for ele in ans:
    print(ele)
