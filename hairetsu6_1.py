# 配列の要素の長さ、値の最大値、最小値、合計、値の要素の数、要素が一致した最初の位置
# 要素の存在確認処理
# 新規作成 2023/3/7

scores = [10, 20, 30, 20, 40]

print(len(scores))
print(min(scores))
print(max(scores))
print(sum(scores))

print(scores.count(20))
print(scores.index(20))
print(20 in scores)
print(100 in scores)
