n, k = map(int, input().split())
a = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(k):
        if a[i][j] == "1":
            print(i + 1, j + 1)
            break
