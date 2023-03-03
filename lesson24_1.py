# 新規作成 2023/3/3
# NONE変数を使う

# 1回はループに入るため、ansに「NONE」を格納する。
ans = None

ans = int(input("Input Number 1,2,0(Exit)"))
while ans != 0:
  match ans:
    case 1:
      print("menu 1")
    case 2:
      print("menu 2")
    case _:
      print("Invalid Number");
  ans = int(input("Input Number 1,2,0(Exit)"))
