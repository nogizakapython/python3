# 配列のソート処理
# 新規作成 2023/3/7

scores = [10, 20, 30, 20, 40]

#scores.reverse()
#print(scores)
#scores.sort()
#print(scores)

#破壊的
#scores.sort(reverse=True)
#print(scores)

#非破壊的
scores_sorted = sorted(scores,reverse=True)
print(scores_sorted)

scores_sorted1 = sorted(scores,reverse=False)
print(scores_sorted1)
