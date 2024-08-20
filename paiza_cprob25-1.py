N, M = [int(i) for i in input().split()]

for _ in range(M):
    x = int(input())
    ans = -100000

    for w in range(1, 1201):
        if w % N != 0:
            continue
        
        if abs(x - w) <= abs(x - ans):
            ans = w

    print(ans)