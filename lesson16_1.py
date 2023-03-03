# 新規作成 2023/3/3
# match構文

color = ""
while True:
  try:
    i_color = input("色を文字で入力してください")
    color = i_color
    break;
  except:
    print("文字列を入力してください");

match color:
  case "red":
    print("Stop")
  case "yellow":
    print("Slow Down")
  case "blue" | "green":
    print("Go!")
  case _:
    print("Invalid Color")


