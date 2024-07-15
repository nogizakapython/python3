x, y, z = map(int, input().split())

ans = z

for num_x in range(z // x + 1):
    for num_y in range(z // y + 1):
        if num_x * x + num_y * y <= z:
            num_one = z - num_x * x - num_y * y
            if num_x + num_y + num_one < ans:
                ans = num_x + num_y + num_one

print(ans)
