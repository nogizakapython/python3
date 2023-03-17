# coding: utf-8
# クラスを作成する

class Player:
    def __init__(self,name):
        self._name = name
    def walk(self):
        print(f"{self._name}勇者は荒野を歩いていた")



player1 = Player("秋元真夏")
player1.walk()
