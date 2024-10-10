n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

pos_of_x = -1
for i in range(n):
    if a[i] == x:
        pos_of_x = i + 1
        break

print(pos_of_x)
