n, a, b, mod = map(int, input().split())

for i in range(n):
    x = int(input())
    print((a * x + b) % mod)