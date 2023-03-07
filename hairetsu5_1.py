# 配列の削除
# 新規作成 2023/3/7

# scores配列の定義
scores = [10, 20, 30, 50, 40]

#配列の要素をすべて削除する
#scores.clear()

#配列の要素1つを削除する
#scores.remove(20)

# 指定された配列の要素を削除する
popped_item = scores.pop(3)
# del scores[1]
print(scores)
print(popped_item)
