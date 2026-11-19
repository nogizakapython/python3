a, b, c, d = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(5)]
s = [[0] * 6 for _ in range(6)]

for i in range(5):
    for j in range(5):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

print(s[c + 1][d + 1] - s[a][d + 1] - s[c + 1][b] + s[a][b])