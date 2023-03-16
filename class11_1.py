# クラスのオーバーロード
# 新規作成 2023/3/16

class Post: # 親クラス Superクラス
    def __init__(self, text):
        self._text = text
        self._likes = 0

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

class SponsoredPost(Post): # 子クラス Subクラス
    def __init__(self,text,sponsor):
        # self._text = text
        # self._likes = 0
        super().__init__(text)
        self._sponsor = sponsor

    # オーバーロード
    def show(self):
        print(f"{self._text} - {self._likes} sponsored by {self._sponsor}")

posts = [
    Post("Hello"),
    Post("Hi"),
    SponsoredPost("Hey","dotinstall"),
]

posts[2].like()
for post in posts:
    post.show()

