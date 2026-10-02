N, X, Y = map(int, input().split())
a = [int(x) for x in input().split()]
s = [0] * (N + 1)

for i in range(N):
    s[i + 1] = s[i] + a[i]

print(s[Y + 1] - s[X])
