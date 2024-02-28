from bycycle import Bycycle

class ElectricBycycle(Bycycle):

  # コンストラクタ
  def __init__(self,name="人"):

    self.__name = name

  def electronic_ride(self,name):

    print(f"{name}は電動自転車を漕ぐ")

