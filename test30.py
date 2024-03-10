import sys

class Animal():
  def __init__(self,name,avg_age):
    self.__name = name
    self.__avg_age = avg_age

  @property
  def get_avg_age(self):
    return self.__avg_age

  @get_avg_age.setter
  def set_avg_age(self,avg_age):
    try:
      avg_age = int(avg_age)
    except ValueError:
      print("文字を入力するな")
      sys.exit()
    if avg_age <= 0:
      print("負の数と0を入力しないでください。")
      sys.exit()
    self.__avg_age = avg_age

