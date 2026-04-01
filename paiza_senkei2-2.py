n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k = -1
for i in range(n):
    if a[i] == k:
        index_of_k = i
        break

print(index_of_k + 1)