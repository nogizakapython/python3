values = input().split()
K = int(values[0])
L = int(values[1])

A = [[0] * 3 for _ in range(3)]
for i in range(3):
    values = input().split()
    for j in range(3):
        A[i][j] = int(values[j])

print(A[K - 1][L - 1])
