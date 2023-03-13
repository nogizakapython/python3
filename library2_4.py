# ライブラリ randintしか使用しない
# 新規作成 2023/3/13
from random import randint


num = randint(1,6)
match num:
  case 1:
    print("1")
  case 2:
    print("2")
  case 3:
    print("3")
  case 4:
    print("4")
  case 5:
    print("5")
  case 6:
    print("6")

