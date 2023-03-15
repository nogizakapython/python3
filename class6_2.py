# クラスのカプセル化検証
# 新規作成:2023/3/15

# クラスの作成
class Nogizaka1:
    # コンストラクタ
    def __init__(self, name):
        self._name = name
        self._likes = 0
    
    # showメソッド
    def show(self):
        print(f"{self._name}さんのいいねの数は{self._likes}です。")
    
    # likeメソッド
    def like(self):
        self._likes += 1

# インスタンスを読み込む

n1 = Nogizaka1("遠藤さくら")
n2 = Nogizaka1("中西アルノ")


for i in range(1,11):
    n1.like()
    i += 1
n1.show()
j=0

for j in range(1,2):
    n2.like()
    j += 1

n2.show()    
