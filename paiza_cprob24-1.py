N, M = map(int, input().split())

W = int(input())

for i in range(1, 1501):
    if i % N == 0:
        print(i, abs(i - W))