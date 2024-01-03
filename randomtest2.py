####################################################
###   入出力テスト
####################################################

import random
array1 = []
array2 = []
N = 0
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

for i in range(0,N):
  name = input("名前を入力してください\n")
  array1.append(name)


for j in range(0,N):
  title = input("プレゼンのお題を入力してください\n")
  array2.append(title)

random_array1 = random.sample(list(set(array1)),N)
random_array2 = random.sample(list(set(array2)),N)

for man in list(random_array1):
  print(man)

for title in list(random_array2):
  print(title)

