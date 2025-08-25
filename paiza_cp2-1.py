N = int(input())
num = N
match N:
    case  num if num < 2:
      print("clear")
    case num if num < 9:
      print("sunny")
    case num if num <= 10:
      print("cloudy")
