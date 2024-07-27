N, M = map(int, input().split())

stock = {}
for _ in range(N):
    a, b = input().split()
    stock[a] = int(b)

for _ in range(M):
    s = input()
    if s in stock:
        print(stock[s])
    else:
        print(-1)
