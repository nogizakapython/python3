n = int(input())
a = [int(x) for x in input().split()]

index_of_odd = 0
for i in range(n - 1, -1, -1):
    if a[i] % 2 == 1:
        index_of_odd = i + 1
        break

print(index_of_odd)
