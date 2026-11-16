N, M = map(int, input().split())
A, B, C = map(int, input().split())
a = []
for i in range(N):
    a.append(int(input()))
print(N + 1)
print(M + 1)
print(A + 1)
print(B + 1)
print(C + 1)
for i in range(N):
    print(a[i] + 1)