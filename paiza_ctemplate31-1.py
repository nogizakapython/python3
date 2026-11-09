N, M = map(int, input().split())
a = []
for i in range(M):
    a.append(int(input()))
print(N + 1)
print(M + 1)
for i in range(M):
    print(a[i] + 1)