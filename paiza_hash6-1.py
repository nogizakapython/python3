table = [[] for i in range(10)]

n = int(input())

for i in range(n):
    x = int(input())
    hash = x % 10
    table[hash].append(x)

for i in range(10):
    print(" ".join(map(str, table[i])))