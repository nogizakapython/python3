# クラスのインスタンスの数を表示する
# 新規作成 2023/3/16

class Post:
    _count = 0

    def __init__(self, text):
        self._text = text
        self._likes = 0
        Post._count += 1

    @classmethod
    def show_count(cls):
        print(f"{cls._count} instance created")

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

posts = [
    Post("Hello"),
    Post("Hi"),
]

for post in posts:
    post.show()

Post.show_count()
