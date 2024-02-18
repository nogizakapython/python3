class Nogizaka46:



  # コンストラクタ
  def __init__(self,name,div="3期生です"):
    self.name = name
    # アクセス制限を指定
    self.__div = div


  # getter Div
  @property
  def getDiv(self):
    return self.__div
  # getter name
  @property
  def getName(self):
    return self.name

  @getDiv.setter
  def setDiv(self,div1):
    if div1 >= 3 and div1 < 6:
      self.__div = str(div1) + "期生です"
    else:
      self.__div = "乃木坂46の現役メンバーではありません"

mem1 = Nogizaka46("梅澤美波")
mem1.setDiv = 3
name1 = mem1.getName
div1= mem1.getDiv
print(f'{name1}は{div1}')

mem2 = Nogizaka46("中西アルノ")
name2 = mem2.getName
mem2.setDiv = 5
div2= mem2.getDiv
print(f'{name2}は{div2}')

mem3 = Nogizaka46("桜井玲香")
name3 = mem3.getName
mem3.setDiv = 1
div3= mem3.getDiv
print(f'{name3}は{div3}')

mem4 = Nogizaka46("岩本蓮加")
name4 = mem4.getName
div4= mem4.getDiv
print(f'{name4}は{div4}')



