####################################################
###   お題抽選ツール
####################################################

#ランダムモジュールを呼び出す
import random
#配列を定義する
array1 = []
array2 = []
#人数変数
N = 0
#正の整数が入力されるまで繰り返す
while True:
  try:
    N = int(input("登録人数を指定してください\n"))
    if N <= 0:
      raise ValueError("error!")
    else:
      break
  except ValueError as e:
    print("文字列、小数、負の整数、0を入力しないでください")
    print("正の整数を入力してください")

#配列に名前を登録する
for i in range(0,N):
  name = input("名前を入力してください\n")
  array1.append(name)

#配列にお題を登録する
for j in range(0,N):
  title = input("プレゼンのお題を入力してください\n")
  array2.append(title)

#配列の要素をランダムに並べる
random_array1 = random.sample(list(set(array1)),N)
random_array2 = random.sample(list(set(array2)),N)

#ランダムに並べた名前を1行ずつ出力する。
for man in list(random_array1):
  print(man)

#ランダムに並べたお題を1行ずつ出力する
for title in list(random_array2):
  print(title)

