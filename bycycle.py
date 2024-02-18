class Bycycle:

  # コンストラクタ
  def __init__(self,name="人"):

    self.__name = name



  # getter Div
  # getter name
  @property
  def getName(self):
    return self.__name

  @getName.setter
  def setName(self,set_name):
     if len(set_name) > 0:
        self.__name = set_name


  def riding(self,set_name):
    print(f"{set_name}は自転車を漕ぐ")

  def breaking(self,set_name):
    print(f"{set_name}はブレーキをかけて止まる")
