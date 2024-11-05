a = [1] * (40 + 1)

for i in range(3, 40 + 1):
    a[i] = a[i - 1] + a[i - 2]

k = int(input())
print(a[k])
