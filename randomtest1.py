####################################################
###   入出力テスト
####################################################


while True:
  try:
    N = int(input("登録人数を指定してください\n"))
    if N < 0:
      raise ValueError("error!")
    else:
      break
  except ValueError as e:
    print("文字列、小数、負の整数を入力しないでください")
    print("正の整数を入力してください")
