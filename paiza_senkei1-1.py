n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

num_of_k = 0
for val in a:
    if val == k:
        num_of_k += 1

print(num_of_k)