N = int(input())

if N % 400 == 0:
    print("Leap")
elif N % 100 == 0:
    print("Common")
elif N % 4 == 0:
    print("Leap")
else:
    print("Common")