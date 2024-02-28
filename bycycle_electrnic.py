from bycycle import Bycycle

class ElectricBycycle(Bycycle):
  def __init__(self, name="人"):
    self.__name = super().__init__(name)

  def electronic_ride(self):

    print(f"{self.__name}は電動自転車を漕ぐ")

