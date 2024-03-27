n = int(input())
count = 0
while True:
    odd = n % 2
    n /= 2
    if odd == 0:
        count += 1
    else:
        break

print(count)
