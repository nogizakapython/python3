class MenuItem:
    # info メソッドを定義してください
    def info(self):
      print('メニューの名前と値段が表示されます')


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1 に対して info メソッドを呼び出してください
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2 に対して info メソッドを呼び出してください
menu_item2.info()
