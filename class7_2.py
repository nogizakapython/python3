# setter getter
# 新規作成 2023/3/16
# setter、getterの動作確認

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

rei1 = Post("中西アルノ")

# posts[0]._likes = 100
# print(posts[0]._likes)

rei1.set_likes(10)

t = 0
for t in range(0,2):
    rei1.like()

rei1.show()

rei2 = Post("川﨑桜")
rei2.set_likes(1)

u = 0

while u < 2:
    rei2.like()
    u += 1

rei2.show()
