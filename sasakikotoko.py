# 佐々木琴子さんツイート用BOT作成ツール

food = ""
while True:
  print("今日美味しかった食べ物を入力してください。")
  food = input()
  food = food.replace("　","")
  check_food = food.replace(" ","")
  food_length = len(check_food)
  if food_length == 0:
    print("文字が入力されていません")
  elif food_length > 0:
    break

answer_sentense = f"今日は{food}を食べました。美味しかったです。"
print(answer_sentense)
