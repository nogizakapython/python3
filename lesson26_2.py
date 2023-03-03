# 新規作成 2023/3/3
# break、continue処理
# while False処理でループに入らない


while False:
  ans = int(input("Input Number 1,2,3,0(Exit)"))
  match ans:
    case 1:
      print("menu 1")
    case 2:
      print("menu 2")
    case 3:
      print("menu 3")
    case 0:
      break
    case _:
      print("Invalid Number");
      continue
  print("Correct Number Process")

