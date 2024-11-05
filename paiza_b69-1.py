x, d1, d2 = map(int, input().split())

a = [x] * (1000 + 1)

for i in range(2, 1000 + 1):
    if i % 2 == 0:
        a[i] = a[i - 1] + d2
    else:
        a[i] = a[i - 1] + d1

q = int(input())

for i in range(q):
    k = int(input())
    print(a[k])
