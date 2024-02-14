class Computer:
  # コンストラクタ
  def __init__(self,name='Windows',memory=50):
    self.name = name
    # アクセス制限を指定
    self.__memory = memory

  # getter
  @property
  def getMemory(self):
    return self.__memory

  @property
  def getName(self):
    return self.name

  @getMemory.setter
  def setMemory(self,value):
    if value > 100:
      self.__memory = value
    else:
      self.__memory = 100

com1 = Computer()
com1.setMemory = 20
sum = com1.getMemory
name = com1.getName
print(f'{name}のメモリ量は{sum}GBです')
