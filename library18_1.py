# タプルデータを集計する
# 新規作成 2023/3/15

# defaultdictライブラリを使う
from collections import defaultdict

# タプルデータ
results = [
    ("pass", "Taro"),
    ("pass", "Jiro"),
    ("fail", "Saburo"),
    ("pass", "Shiro")]
# stats = {"pass": ["Taro", "Jiro", "Shiro"], "fail": ["Saburo"]}

# 辞書配列を宣言する
stats = defaultdict(list)

for result,name in results:
    # 辞書に追加する
    stats[result].append(name)
    
print(dict(stats))    