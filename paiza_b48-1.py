string = input()
alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

first = string[0]
last = string[len(string) - 1]

flag = False
for alphabet in alphabets:
    if first == alphabet:
        flag = True

    if flag:
        print(alphabet)

    if last == alphabet:
        break
