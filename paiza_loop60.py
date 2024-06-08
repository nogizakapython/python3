
for x in range(0,24):
    for y in range(0,60):
        ans = x + y
        msg = ""
        match ans:
            case ans if ans % 3 == 0 and ans % 5 == 0:
                msg = "FizzBuzz"
            case ans if ans % 3 == 0:
                msg = "Fizz"
            case ans if ans % 5 == 0:
                msg = "Buzz"
            case _:
                msg = ""
        print(f"{x} 時{y} 分の鳩時計の鳴き声{msg}")

