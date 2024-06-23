N = int(input())

X = [0] * N
Y = [0] * N
for i in range(N):
    values = input().split()
    X[i] = int(values[0])
    Y[i] = int(values[1])

for i in range(N):
    print(abs(X[i] - 2) + abs(Y[i] - 3))
