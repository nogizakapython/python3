# defaultdictライブラリを使う
# 新規作成 2023/3/15

# defaultdictライブラリを読み込む
from collections import defaultdict
# 集計対象の配列
results = ["pass", "pass", "fail", "pass", "fail", "pass"]

def init():
    return 0


stats = defaultdict(init)
for result in results:
    # if result not in stats:
    #     stats[result] = 0
    stats[result] += 1

print(stats)
print(dict(stats))
