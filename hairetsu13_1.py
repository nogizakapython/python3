# タプル
# 要素の変更ができない
# 新規作成 2023/3/7
# in,len(),index(),count() →使える
# append(),insert(),pop() → 使えない

# タプルの定義
# tokyo = ("JPY",36,140)
nagoya = "JPY",35,137

print(nagoya)
print(nagoya[0])
print(nagoya[1])
print(nagoya[2])

print(len(nagoya))


# タプルをリストに変換
nagoya2 = list(nagoya)
print(nagoya2)


# リストをタプルに変換
nagoya3 = tuple(nagoya2)
print(nagoya3)
