board = []
result = "D"

for i in range(5):
    board.append(input())

for i in range(5):
    pivot = ""
    count = 0

    for j in range(5):
        stone = board[j][i]

        if pivot == "":
            pivot = stone

        if stone != "." and stone == pivot:
            count += 1
        else:
            break

    if count == 5:
        result = pivot
        break


print(result)
