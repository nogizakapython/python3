# 位置引数とキーワード引数
# 新規作成 2023/3/3

def greet(name,by):
    print(f"{by} Hi! {name}")

#キーワード引数
greet(name="Taro",by="John")
greet(name="Jiro",by="Rich")
#位置引数
greet("Manatsu","Mai")
