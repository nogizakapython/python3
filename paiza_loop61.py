ans = 0
for x in range(1, 100):
    for y in range(1, 100 - x):
        if ans < x * y and x ** 3 + y ** 3 < 100000:
            ans = x * y

print(ans)
