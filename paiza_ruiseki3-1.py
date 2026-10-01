X, Y = map(int, input().split())
a = [int(x) for x in input().split()]
s = [0] * 11

for i in range(10):
    s[i + 1] = s[i] + a[i]

print(s[Y + 1] - s[X])