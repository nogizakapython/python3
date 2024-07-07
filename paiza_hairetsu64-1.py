n = int(input())
a = [int(input()) for _ in range(n)]
x, y = map(int, input().split())

tmp = a[x - 1]
a[x - 1] = a[y - 1]
a[y - 1] = tmp

for i in a:
    print(i)
