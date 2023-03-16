# クラスの継承
# 新規作成 2023/3/16

# 親クラス(スーパークラス)
class Post:
    def __init__(self, text):
        self._text = text
        self._likes = 0

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

# 子クラス(サブクラス)
class SponsoredPost(Post):
    pass

posts = [
    Post("Hello"),
    Post("Hi"),
    SponsoredPost("Hey"),
]

for post in posts:
    post.like()
    post.show()

