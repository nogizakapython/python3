for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="")
        if j != 9:
            print(" ", end="")
    print()
