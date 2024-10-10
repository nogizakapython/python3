m, n = map(int, input().split())
a = []
for i in range(m):
    a.append([int(t) for t in input().split()])
x = [int(t) for t in input().split()]

pos_of_x = -1
for i in range(m):
    is_x = True
    for j in range(n):
        if a[i][j] != x[j]:
            is_x = False

    if is_x:
        pos_of_x = i + 1
        break

print(pos_of_x)
