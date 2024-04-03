N = int(input())

binary = 0
i = 0
while N > 0:
    digit_num = N % 2
    binary += digit_num * pow(10, i)
    print(binary)
    N //= 2
    i += 1

print(binary)
