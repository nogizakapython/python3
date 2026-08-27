n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

answer = 101
for val in a:
    if val >= k:
        answer = min(answer, val)

print(answer)
