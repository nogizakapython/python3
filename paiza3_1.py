# coding: utf-8
# 変数をクラスで管理する

class Player:
    def __init__(self,job):
        self.job = job


    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

player1.walk()
