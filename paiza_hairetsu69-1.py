n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(i):
        print(a[i] * a[j])
