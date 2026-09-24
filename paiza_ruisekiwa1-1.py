a = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
s = [0] * 11

for i in range(10):
    s[i + 1] = s[i] + a[i]

print(s[8] - s[2])
