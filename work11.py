# 新規作成 2023/3/7
# 配列の追加、削除

members = []
w_array = []

def array_del():
  w_array.clear()



# 追加する要素を入力する
str = input("スペースで区切って要素を複数追加する")
members = str.strip().split(" ")

print(members)
str2 = input("要素を追加してください")
w_array = str2.strip().split(" ")
# 配列に要素を追加する(複数も指定できる)
members.extend(w_array)
print(members)


# 配列の要素をすべて削除する
array_del()

# 配列の要素の1番目に要素を追加する
str3 = input("要素を追加してください")
w_array = str3.strip().split(" ")
members.insert(1,w_array)
print(members)
