# 文字列を区切り文字で分割して配列に格納する
# 配列から文字列を作成する

# 文字列を配列に格納する
birthday = "2011-11-27"
array1 = birthday.split("-")
print(array1)

# 配列から文字列に変換する
birthday2 = ["2022","11","27"]
print("-".join(birthday2))

# 数値要素の配列を文字に変換して文字列にする
birthday3 = [1993,8,20]
print("-".join([str(n) for n in birthday3]))
