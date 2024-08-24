N, K = map(int, input().split())
roster = { (x,y) for x, y in [input().split() for _ in range(N)]}

for _ in range(K):
    q = input()
    for num, ID in roster:
        if num == q:
            print(ID)
