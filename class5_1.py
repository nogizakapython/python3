# クラスのメソッドの挙動の検証
# 新規作成:2023/3/15

# クラスの作成
class Post:
    # コンストラクタ
    def __init__(self, text):
        self.text = text
        self.likes = 0
    
    # showメソッド
    def show(self):
        print(f"{self.text} - {self.likes}")
    
    # likeメソッド
    def like(self):
        self.likes += 1

# インスタンスを読み込む
posts = [
    Post("Hello"),
    Post("Hi"),
]

# posts[0].likes += 1
# いいねを1加算する
posts[0].like()

# ループで処理をする
for post in posts:
    post.show()
