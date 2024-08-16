a = input()
n = int(input())

for i in range(n):
    b = input()

    if a == b:
        print("first")
    elif abs(int(a) - int(b)) == 1:
        print("adjacent")
    elif a[2:] == b[2:]:
        print("second")
    elif a[3:] == b[3:]:
        print("third")
    else:
        print("blank")
