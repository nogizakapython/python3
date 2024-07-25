H, W, r, c = map(int, input().split())
maze = [input() for _ in range(H)]

if maze[r-1][c-1] == "#":
    print("Yes")
else:
    print("No")
