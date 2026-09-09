n = int(input())
results = [input().split() for _ in range(n)]
k = int(input())

for name, score in results:
    if int(score) >= k:
        print(name)
