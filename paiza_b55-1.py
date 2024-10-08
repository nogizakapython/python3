board = []
result = "D"
direction = [True, False]

for i in range(5):
    board.append(input())

for reverse in direction:
    pivot = ""
    count = 0

    if reverse:
        j = 0
        j_diff = 1
    else:
        j = 4
        j_diff = -1

    for i in range(5):

        stone = board[i][j]

        if pivot == "":
            pivot = stone

        if stone != "." and stone == pivot:
            count += 1

        j = j + j_diff

    if count == 5:
        result = pivot
        break

print(result)
