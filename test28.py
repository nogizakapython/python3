# 配列リターンテスト

# 配列に要素を追加するクラス
class Test1():
  # コンストラクタ
  def __init__(self):
    self.__name = ""

  # 配列にsetterから渡された名前を、呼び出した配列に追加する
  def append_test(self,list1):
      list1.append(self.__name)
      return list1

  # setter
  def set_name(self,name):
    self.__name = name


def main():
  nogizaka_member = []

  for name in ["梅澤美波","山下美月","遠藤さくら","井上和","田村真佑"]:
    t = Test1()
    t.set_name(name)
    nogizaka_member = t.append_test(nogizaka_member)

  for number,name2 in enumerate(nogizaka_member,1):
    print(number,name2)

if __name__ == "__main__":
  main()
