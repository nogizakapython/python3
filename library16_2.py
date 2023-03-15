# defaultdictライブラリの利用
# 新規作成 2023/3/15
# ラムダ関数を使う

# defaultdictライブラリを使う
from collections import defaultdict
results = ["pass", "pass", "fail", "pass", "fail", "pass"]

# def init():
#     return 0


# stats = defaultdict(init)
stats = defaultdict(lambda:0)
# stats = defaultdict(int)
for result in results:
    # if result not in stats:
    #     stats[result] = 0
    stats[result] += 1

print(stats)
print(dict(stats))
