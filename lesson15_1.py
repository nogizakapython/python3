# 新規作成 2023/3/2
# 論理演算子

eng_score = int(input("英語の点数を入力してください"))
math_score = int(input("数学の点数を入力してください"))

if eng_score == 100 and math_score == 100:
  print("Excelent")

if eng_score == 100 or math_score == 100:
  print("OK")

if not (eng_score == 0 or math_score == 0):
  print("not redpoint")
else:
  print("redpoint")
