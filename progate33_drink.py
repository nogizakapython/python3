from progate33menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
