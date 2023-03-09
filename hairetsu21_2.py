# リストから辞書に変換する
# zipメソッドを使う
# 新規作成 2023/3/9

keys = ["math", "english", "physics"]
values = [62, 91, 84]

scores={}
for key,value in zip(keys,values):
    scores[key] = value

print(scores)
