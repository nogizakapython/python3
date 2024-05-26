n = int(input())

ans = 0
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1

print(ans)
