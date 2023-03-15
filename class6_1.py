# クラスのカプセル化
# 新規作成 2023/3/15


class Post:
    def __init__(self, text):
        self._text = text
        self._likes = 0
    
    def show(self):
        print(f"{self._text} - {self._likes}")
    
    def like(self):
        self._likes += 1

posts = [
    Post("Hello"),
    Post("Hi"),
]

# posts[0]._likes += 1
posts[0].like()

for post in posts:
    post.show()
