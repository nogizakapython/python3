n = int(input())
points = [[int(x) for x in input().split()] for _ in range(n)]
xs, xt = [int(x) for x in input().split()]
ys, yt = [int(x) for x in input().split()]

answer = 0

for xi, yi in points:
    horizontal = xs <= xi <= xt
    vertical = ys <= yi <= yt
    if horizontal and vertical:
        answer += 1

print(answer)