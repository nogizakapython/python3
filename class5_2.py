# クラスのメソッドの挙動の検証
# 新規作成:2023/3/15

# クラスの作成
class Nogizaka1:
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        self.likes = 0
    
    # showメソッド
    def show(self):
        print(f"{self.name}さんのいいねの数は{self.likes}です。")
    
    # likeメソッド
    def like(self):
        self.likes += 1

# インスタンスを読み込む

n1 = Nogizaka1("遠藤さくら")
n2 = Nogizaka1("中西アルノ")


i=0
while i < 10:
    n1.like()
    i += 1
n1.show()
j=0
while j < 1:
    n2.like()
    j += 1

n2.show()    
