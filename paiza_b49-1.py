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
result = "true"

first = string[0]
last = string[len(string) - 1]

for alphabet in alphabets:
    if first == alphabet:
        break

    if last == alphabet:
        result = "false"

print(result)
