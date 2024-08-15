n = int(input())

re = []

for i in range(n):
    s = input()

    if s in re:
        re.pop(re.index(s))

    re.append(s)

for i in range(len(re)):
    print(re[-i - 1])