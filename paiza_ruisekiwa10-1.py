a = [int(x) for x in input().split()]
b = [0] * 10
s = [0] * 11

for i in range(10):
    if a[i] % 2 == 0:
        b[i] = 1

for i in range(10):
    s[i + 1] = s[i] + b[i]

print(s[8] - s[2])