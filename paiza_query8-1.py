N, X, P = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.append(X)
A.append(P)
print(sorted(A).index(P) + 1)
