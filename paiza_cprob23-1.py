N, M = map(int, input().split())

P = int(input())
K = list(map(int, input().split()))

for _ in range(M):
    w = int(input())
    ans = -100000  # 絶対に答えにならないもので初期化

    for i in range(P):
        if K[i] % N == 0:
            if abs(K[i] - w) <= abs(ans - w):
                ans = K[i]

    print(ans)