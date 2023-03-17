# coding: utf-8
# RPGの敵クラスを作る

# coding: utf-8
# RPGの敵クラスを作る

class Enemy:
    def __init__(self,name):
        self.name = name

    def attack(self,enemy):
        print(self.name + "は" + enemy + "を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack("衛藤美彩")
