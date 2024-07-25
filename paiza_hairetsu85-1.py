N = int(input())
A = [int(x) for x in input().split()]

count = [0] * 10
for num in A:
    count[num] += 1

print(" ".join(map(str, count)))
