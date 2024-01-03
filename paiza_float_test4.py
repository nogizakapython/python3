# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
while True:
  try:
    num = int(input("データ数を正の整数で入力してください"))
    if num < 1:
      raise ValueError
    else:
      break
  except ValueError as e:
      print("正の整数以外は入力しないでください")

for i in range(0,num):
    data1 = input()
    array1 = data1.split(' ')
    N = float(array1[0])
    M = int(array1[1])
    try:
      ans = "{:.{}f}".format(N,M)
    except:
      print("無効")
    print(ans)
