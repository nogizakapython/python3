# シャッフルライブラリ
# 新規作成 2023/3/13

# randomライブラリの読み込み
import random

# names配列
names = ["Taro", "Jiro", "Saburo", "Shiro", "Goro"]

# 要素の順番をシャッフルする
random.shuffle(names)
print(names)

# 要素の中から1つを取り出す
name1 = random.choice(names)
print(name1)

# 要素の中から重複を許して要素3つ取り出す
winners = random.choices(names,k=3)
print(winners)

# 要素の中から重複を許さず要素3つ取り出す
names = list(set(names))
winners2 = random.sample(names,3)
print(winners2)
