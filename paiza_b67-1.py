# 1 行の入力を文字列として受け取り、半角スペースで区切ったものを整数に変換する
H, W, N = map(int, input().split())

# 1 行の入力を文字列として受け取り、半角スペースで区切ったものを整数の配列に変換する
# この操作を H 回繰り返す
cards = [list(map(int, input().split())) for _ in range(H)]

# H 行の配列を 1 つずつ取り出して処理する
for line in cards:
  # join 関数を使うために整数の配列を文字列の配列に変換
  line = map(str, line)
  # join 関数で line 配列の要素を半角スペース区切りで連結した文字列に変換
  print(' '.join(line))
