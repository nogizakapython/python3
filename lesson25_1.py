# 新規作成 2023/3/3
# NONE変数を使う
# break、continue処理
# 1回はループに入るため、ansに「NONE」を格納する。
ans = None


while True:
  ans = int(input("Input Number 1,2,0(Exit)"))
  match ans:
    case 1:
      print("menu 1")
    case 2:
      print("menu 2")
    case 0:
      break
    case _:
      print("Invalid Number");
      continue
  print("Correct Number Process")

