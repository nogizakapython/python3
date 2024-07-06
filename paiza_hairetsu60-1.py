n = int(input())
numbers = [0] * 101
ans = 0

for _ in range(n):
    a = int(input())
    if numbers[a] == 0:
        ans += 1
        numbers[a] = 1

print(ans)
