table = [[] for i in range(100)]

a, b = map(int, input().split())
q = int(input())

for i in range(q):
    op, x = map(int, input().split())
    hash = (a * x + b) % 100

    if op == 1:
        table[hash].append(x)
    elif op == 2:
        if x in table[hash]:
            print("Yes")
        else:
            print("No")

for i in range(100):
    print(" ".join(map(str, table[i])))