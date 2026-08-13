N = int(input())

is_prime = True
a = 2
fermat = 1

if N % a == 0:
    is_prime = False

for i in range(N - 1):
    fermat *= a
    fermat %= N

if fermat % N != 1:
    is_prime = False

if is_prime:
    print("YES")
else:
    print("NO")