# 新規作成 2023/3/16
# @「プロパティ」を使ったsetter,getter処理

class Post:
    def __init__(self, text):
        self._text = text
        self._likes = 0

    def show(self):
        print(f"{self._text} - {self._likes}")

    def like(self):
        self._likes += 1

    # # setter
    # def set_likes(self, num):
    #     self._likes = num

    # # getter
    # def get_likes(self):
    #     return self._likes

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self,num):
        self._likes = num

posts = [
    Post("Hello"),
    Post("Hi"),
]

# posts[0]._likes = 100
# print(posts[0]._likes)

posts[0].likes = 100
print(posts[0].likes) # 100

# for post in posts:
#     post.show()

