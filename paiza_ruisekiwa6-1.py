a = [int(x) for x in input().split()]
s = [0] * 11

for i in range(10):
    s[i + 1] = s[i] + a[i]

max_sum = 0

for i in range(8):
    max_sum = max(max_sum, s[i + 3] - s[i])

print(max_sum)
