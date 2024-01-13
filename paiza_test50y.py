values = input().split()
H = int(values[0])
W = int(values[1])
A = int(values[2])
B = int(values[3])

for i in range(H):
    for j in range(W):
        print(f"({A:>9}, {B:>9})", end="")
        if j == W - 1:
            print()
        else:
            print(end=" | ")

    if i < H - 1:
        print("=" * (22 * W + 3 * (W - 1)))
