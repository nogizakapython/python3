# 配列の要素で条件式を満たした場合、ループ処理を抜けて終了する

numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # 変数 number が 777 のとき「 777が見つかったので処理を終了します 」と出力した後、処理を終了させてください
    if number == 777:
      print("777が見つかったので処理を終了します")
      break