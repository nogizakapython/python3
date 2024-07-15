n = int(input())

flag = False
for b in range(1, n):
    for c in range(1, n - b):
        a = n - b - c
        if a ** 2 == b ** 2 + c ** 2:
            flag = True

if flag:
    print("YES")
else:
    print("NO")
