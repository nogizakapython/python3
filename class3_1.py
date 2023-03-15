# クラスの作成
# 新規作成:2023/3/15

# クラスの定義
class Post:
    # コンストラクタ
    def __init__(self,text,likes):
        self.text = text
        self.likes = likes

# インスタンスを呼び出す
posts = [
    Post("Hello",3),
    Post("Hi",5),
    
]

#出力 
print(posts[0].text)
print(posts[0].likes)
print(posts[1].text)
print(posts[1].likes)
