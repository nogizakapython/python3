n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

for i in range(n):
    if a[i] == k:
        print(i + 1)