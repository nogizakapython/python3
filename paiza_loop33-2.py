N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if a[i] == 1:
        print(i + 1)
