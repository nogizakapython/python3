# coding: utf-8
# RPGの敵クラスを作る

# coding: utf-8
# RPGの敵クラスを作る

class Enemy:
    def __init__(self,name):
        self.name = name

    def attack(self):
        str = "山下美月"
        print(self.name + "は" + str + "を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack()
