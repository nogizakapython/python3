N = int(input())
a = [int(x) for x in input().split()]
s = [0] * (N + 1)

for i in range(N):
    s[i + 1] = s[i] + a[i]

max_sum = 0

for i in range((N - 3) + 1):
    max_sum = max(max_sum, s[i + 3] - s[i])

print(max_sum)
