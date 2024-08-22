N, Q = map(int, input().split())
A = {int(input()) for _ in range(N)}

for _ in range(Q):
    k = int(input())
    if k in A:
        print("YES")
    else:
        print("NO")
