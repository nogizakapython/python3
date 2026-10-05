N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
print(N + 1)
print(M + 1)
for i in range(N):
    print(a[i] + 1)