# クラスのオーバーロード
# 新規作成 2023/3/16

class Human():
    def __init__(self, name="Jonson", age=20):
        self.name = name
        self._age = age
    def show(self):
        print(f"私の名前は{self.name}です。年齢は{self._age}です。")
    def likes(self):
        self._age += 1
jonson = Human()
jonson.show()
man = Human("taro", 21)
man.show()
woman = Human("mariko")
woman.show()
mika = Human("mika",30)
mika.likes()
mika.show()
