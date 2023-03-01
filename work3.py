# 数当てプログラム2
# 新規作成 2023/3/1
import random
#名前入力表示
print("Input your name ",end="")
# 入力した文字列を変数に渡す
name = input()
#正解の数値を乱数を使って作成
answer = random.randint(1,10)
#カウント回数
count = 0
while True:
  #入力した数値を変数に渡す
  num = int(input("Input your number "))
  count += 1
  if answer == num:
    print(f"{name}さん、{count}回目で正解です")
    break
  elif answer > num:
    print(f"{name}さん、正解はもっと数字が大きいです")
  elif answer < num:
    print(f"{name}さん、正解はもっと数字が小さいです")
