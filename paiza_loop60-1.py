for x in range(0,24):
    for y in range(0,60):
        ans = x + y
        msg = ""
        if ans % 3 == 0 and ans % 5 == 0:
            msg = "FIZZBUZZ"
        elif ans % 3 == 0:
            msg = "FIZZ"
        elif ans % 5 == 0:
            msg = "BUZZ"
        else:
            msg = ""
        if msg == "":
            print()
        else:
            print(msg)

