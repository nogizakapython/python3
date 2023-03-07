# 配列の追加
# insertメソッド、extendメソッドを使う
# 新規作成 2023/3/7

# 配列
old_members = ["白石麻衣","齋藤飛鳥","生田絵梨花"]
# 配列を追加するメソッド
old_members.append("秋元真夏")
# 配列を表示する
print(old_members)

# 配列
new_members = ["中西アルノ","菅原咲月"]
# 配列を追加するメソッド
new_members.extend(["川﨑櫻","池田瑛紗"])
# 配列を表示する
print(new_members)

# 配列
points = [20,10,40,60,35]
# 配列を追加するメソッド
points.insert(0,25)
# 配列を表示する
print(points)



