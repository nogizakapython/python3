board = []

for i in range(5):
    board.append(input())


def row():
    result = "D"

    for line in board:
        pivot = line[0]
        count = 0

        for stone in line:
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def column():
    result = "D"

    for i in range(5):
        pivot = ""
        count = 0

        for j in range(5):
            if pivot == "":
                pivot = board[j][i]

            stone = board[j][i]
            if stone != "." and stone == pivot:
                count += 1
            else:
                break

        if count == 5:
            result = pivot
            break

    return result


def oblique():
    result = "D"
    direction = [True, False]

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

    return result


row = row()
column = column()
oblique = oblique()

if row != "D":
    print(row)
elif column != "D":
    print(column)
elif oblique != "D":
    print(oblique)
else:
    print("D")
