N, X, Y = map(int, input().split())
a = [int(x) for x in input().split()]
b = [0] * N
s = [0] * (N + 1)

for i in range(N):
    if a[i] % 2 == 0:
        b[i] = 1

for i in range(N):
    s[i + 1] = s[i] + b[i]

print(s[Y + 1] - s[X])