# クラスの作成
# 新規作成:2023/3/15

# クラスの定義
class Post:
    # コンストラクタ
    def __init__(self,id,name):
        self.id = id
        self.name = name

# インスタンスを呼び出す
posts = [
    Post(1,"taro"),
    Post(2,"jiro"),
    
]

#出力 
print(posts[0].id)
print(posts[0].name)
print(posts[1].id)
print(posts[1].name)
