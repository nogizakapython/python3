# クラスのインスタンスの数を表示する
# 新規作成 2023/3/16

class Nogizaka:
    _count = 0

    def __init__(self, name,text):
        self._name = name
        self._text = text
        self._likes = 0
        Nogizaka._count += 1

    @classmethod
    def show_count(cls):
        print(f"{cls._count} instance created")

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



nogizakas = [
    Nogizaka("秋元真夏","あなたのハートに、ズッキュン💛"),
    Nogizaka("松村沙友理","さゆりんごパーンチ"),
    Nogizaka("中元日芽香","ひめたんびーむ"),
]

for member in nogizakas:
    member.likes = 0
    member.like()
    member.show()

Nogizaka.show_count()
