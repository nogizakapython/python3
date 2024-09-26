result = "D"

for i in range(5):
    board = input()

    pivot = board[0]
    count = 0
    for stone in board:
        if stone != "." and stone == pivot:
            count += 1
        else:
            break

    if count == 5:
        result = pivot


print(result)
