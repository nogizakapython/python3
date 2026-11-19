N = int(input())
a, b, c, d = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
s = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

print(s[c + 1][d + 1] - s[a][d + 1] - s[c + 1][b] + s[a][b])