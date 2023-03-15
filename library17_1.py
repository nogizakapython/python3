#  Counterライブラリを使う
# 新規作成 2023/3/15

# Counterライブラリを読み込む
from collections import Counter

results = ["pass", "pass", "fail", "pass", "fail", "pass"]

stats = Counter(results)
print(dict(stats))
