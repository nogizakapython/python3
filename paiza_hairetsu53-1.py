values = input().split()
N = int(values[0])
A = int(values[1])
B = int(values[2])

X = [0] * N
Y = [0] * N
for i in range(N):
    values = input().split()
    X[i] = int(values[0])
    Y[i] = int(values[1])

print(abs(X[B - 1] - X[A - 1]) + abs(Y[B - 1] - Y[A - 1]))
