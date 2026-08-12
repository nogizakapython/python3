N = int(input())

is_prime = [True] * (N + 1)

is_prime[0] = False
is_prime[1] = False

for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i * 2, N + 1, i):
            is_prime[j] = False

if is_prime[N]:
    print("YES")
else:
    print("NO")