a = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
s = [0] * 11

for i in range(10):
    s[i + 1] = s[i] + a[i]

max_sum = 0

for i in range(8):
    max_sum = max(max_sum, s[i + 3] - s[i])

print(max_sum)
