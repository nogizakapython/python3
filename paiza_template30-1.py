N, M = map(int, input().split())
a = []
for i in range(N - 1):
    a.append(int(input()))
print(N + 1)
print(M + 1)
for i in range(N - 1):
    print(a[i] + 1)
