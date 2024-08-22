N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.insert(K, Q)

for a in A:
    print(a)
