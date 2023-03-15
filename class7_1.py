# setter getter
# 新規作成 2023/3/15

class Post:
    def __init__(self, text):
        self._text = text
        self._likes = 0
    
    def show(self):
        print(f"{self._text} - {self._likes}")
    
    def like(self):
        self._likes += 1
    
    #setter
    def set_likes(self,num):
        self._likes = num
    
    #getter
    def get_likes(self):
        return self._likes

posts = [
    Post("Hello"),
    Post("Hi"),
]

# posts[0]._likes = 100
# print(posts[0]._likes)

posts[0].set_likes(100)
print(posts[0].get_likes())

for post in posts:
    post.show()

