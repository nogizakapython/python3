N, M = map(int, input().split())

k1, k2 = map(int, input().split())

for _ in range(M):
    w = int(input())

    if abs(k1 - w) < abs(k2 - w):
        print(k1)
    else:
        print(k2)