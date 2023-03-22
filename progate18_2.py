# MenuItem クラスを定義してください
class MenuItem:
  def call(name):
    print(name + "さん、こんにちは")

menu = MenuItem
menu.call("Takao")