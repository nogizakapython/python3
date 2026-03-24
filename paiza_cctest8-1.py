n = int(input())

for i in range(n):
    x = input()

    hash = x.count("p") + x.count("a") + x.count("i") + x.count("z")
    print(hash)