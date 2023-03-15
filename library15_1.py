# 新規作成 2023/3/15
# 集計結果を連想配列に格納する

results = ["pass", "pass", "fail", "pass", "fail", "pass"]
# stats = {"pass":4,"fall":2}

stats = {}

for result in results:
    if result not in stats:
        stats[result] = 0
    stats[result] += 1
    
print(stats)    
    