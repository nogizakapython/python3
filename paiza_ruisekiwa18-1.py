A = [[int(x) for x in input().split()] for _ in range(5)]
s = [[0] * 6 for _ in range(6)]

for i in range(5):
    for j in range(5):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + A[i][j]

print(s[4][4] - s[1][4] - s[4][1] + s[1][1])
