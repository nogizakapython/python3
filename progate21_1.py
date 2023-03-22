class MenuItem:
    # info メソッドを定義してください
    def info(self,name,price):
        self.name = name
        self.price = price
        print(f"メニューの名前は{self.name}、値段は{self.price}円です")


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1 に対して info メソッドを呼び出してください
menu_item1.info(menu_item1.name,menu_item1.price)

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2 に対して info メソッドを呼び出してください
menu_item2.info(menu_item2.name,menu_item2.price)
