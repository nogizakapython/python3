n = int(input())
results = [input().split() for _ in range(n)]
k, l = [int(x) for x in input().split()]

for name, score in results:
    if k <= int(score) <= l:
        print(name)
