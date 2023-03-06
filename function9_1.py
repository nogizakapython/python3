# 関数で処理をまとめる
#  2023/3/6

def show1():
  str = "-"
  print(str * 10)

def show_ad():
  show1()
  print("SALE! 50% OFF!")
  show1()

def show_content():
    print("BREAKING NEWS!")
    print("Two baby pandas born")
    print("at our Zoo!")


show_ad()
show_content()
show_ad()
