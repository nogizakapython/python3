N = int(input())
height_name = []

for _ in range(N):
    height, name = input().split(' ')
    height_name.append((int(height), name))

height_name.sort(reverse=True)

for _, name in height_name:
    print(name)
