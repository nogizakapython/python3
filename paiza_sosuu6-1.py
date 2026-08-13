N = int(input())

is_prime = [True] * 6000001
is_prime[0] = False
is_prime[1] = False

for i in range(2, 6000001):
    if is_prime[i]:
        for j in range(i * 2, 6000001, i):
            is_prime[j] = False

for _ in range(N):
    A = int(input())
    if is_prime[A]:
        print("pass")
    else:
        print("failure")