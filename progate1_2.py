# 連想配列
# 新規作成 2023/3/8

# 配列
fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}


fruits['melon'] = "メロン"
fruits['pain'] = "パイン"

sorted(fruits.items())
print(fruits)
sorted(fruits.items(),reverse=True)
# for 文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「 ◯◯は△△という意味です 」と出力させてください
print(fruits)