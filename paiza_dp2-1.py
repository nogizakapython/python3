x, d = map(int, input().split())

a = [x] * (1000 + 1)

for i in range(2, 1000 + 1):
    a[i] = a[i - 1] + d

q = int(input())

for i in range(q):
    k = int(input())
    print(a[k])
