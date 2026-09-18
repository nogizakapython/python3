table = [-1] * 10

n = int(input())

for i in range(n):
    x = int(input())

    hash = x % 10

    while table[hash] != -1:
        hash = (hash + 1) % 10

    table[hash] = x

for i in range(10):
    print(table[i])