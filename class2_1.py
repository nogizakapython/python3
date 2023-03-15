# クラスを使わずに投稿データを表示する
# 新規作成 2023/3/15

# show関数
def show(post):
    print(f"{post['text']} - {post['likes']}")

#投稿データ配列 
posts = [    
    {"text":"Hello","likes":3},
    {"text":"Hi","likes":5},
]

print(posts)
# 連想配列の要素を表示する関数を呼び出す
show(posts[0])
show(posts[1])