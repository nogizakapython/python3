N, b, c = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
print(N + 1)
print(b + 1)
print(c + 1)
for i in range(N):
    print(a[i] + 1)
