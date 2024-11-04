n = int(input())
b = [list(map(str, input().split())) for l in range(n)]

b.sort(key = lambda pair : int(pair[0]))

for i in range(n):
    print(b[i][0], b[i][1])
