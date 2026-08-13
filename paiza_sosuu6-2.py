N = int(input())

is_prime = [1] * 6000001
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, 6000001):
    if is_prime[i] == 1:
        for j in range(i * 2, 6000001, i):
            is_prime[j] = 0

for _ in range(N):
    A = int(input())
    if is_prime[A] == 1:
        print("pass")
    else:
        print("failure")