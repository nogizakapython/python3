A,B = [int(x) for x in input().split(' ')]
min_value = 100000000000
for i in range(A,B+1):
    for j in range(A,B+1):
        ans = i * j
        if ans < min_value:
            min_value = ans
print(min_value)
