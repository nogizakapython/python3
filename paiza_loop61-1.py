max_value = 0
ans1 = 0
ans2 = 0
for x in range(1, 100):
    for y in range(1, 100 - x):
        ans1 = x * y
        ans2 = pow(x,3) + pow(y,3)
        if  ans1 > max_value and ans2 < 100000:
            max_value = x * y

print(max_value)
