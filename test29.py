# 配列リターンテスト

# 配列に要素を追加するクラス
class Test1():
  # コンストラクタ
  def __init__(self,name="人"):
    self.__name = name

  @property
  def getter_name(self):
    return self.__name

  @getter_name.setter
  def setter_name(self,name):
    name = name.replace(" ","")
    name = name.replace('\t',"")
    if len(name) <= 0:
      raise ValueError("名前を入力してください")
    else:
      self.__name = name

  # 配列にsetterから渡された名前を、呼び出した配列に追加する
  def append_test(self,list1):
      list1.append(self.__name)
      return list1


def main():
  nogizaka_member = []

  for name in ["梅澤美波","山下美月","遠藤さくら","井上和","田村真佑"]:
    t = Test1(name)
    nogizaka_member = t.append_test(nogizaka_member)

  for number,name2 in enumerate(nogizaka_member,1):
    print(number,name2)

if __name__ == "__main__":
  main()
