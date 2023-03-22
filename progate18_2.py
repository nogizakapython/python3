# MenuItem クラスを定義してください
# 新規作成 2023/3/22

class MenuItem:
  def call(name):
    print(name + "さん、こんにちは")

menu = MenuItem
menu.call("Takao")