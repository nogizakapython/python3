# 新規作成 2023/3/16
# @「プロパティ」を使ったsetter,getter処理

class Nogizaka1:
    def __init__(self, name,text):
        self._name = name
        self._text = text
        self._likes = 0

    def show(self):
        print(f"{self._name} - {self._text} - {self._likes}")

    def like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self,num):
        self._likes = num

nog1 = Nogizaka1("遠藤さくら","さくちゃんはかわいい")
nog1.likes = 50
print(nog1.likes) # 100

nog1.show()

nog2 = Nogizaka1("川崎桜","さくたんさん、しゅわしゅわー")


for i in range(0,2):
    nog2.like()

nog2.show()

nog3 = Nogizaka1("一ノ瀬美空","みーきゅんきゅん🎵")


for i in range(0,5):
    nog3.like()

nog3.show()
