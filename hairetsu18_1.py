# 集合
# 要素を重複させない
# 順序は保持されない
# インデックスを利用できない
members = {"Taro","Jiro","Saburo","Taro"}

members.add("Siro")
members.remove("Jiro")
print(members)

print(len(members))
print("Jiro" in members)
#集合からタプルに変更する
frozen_members = frozenset(members)
#frozen_members.add("Goro")
