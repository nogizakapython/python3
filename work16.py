# 新規作成 2023/3/13
# 辞書のソート処理
# メンバー別成績リスト

scores = [
  {"name": "和田まあや", "math": 10, "english": 12},
  {"name": "弓木奈於", "math": 6, "english": 8},
  {"name": "岡本姫奈", "math": 12, "english": 11},
  {"name": "金川紗耶", "math": 14, "english": 9},
  {"name": "中村麗乃", "math": 7, "english": 10},
]

print("Name          Math        English")
print("------------ ------------ ------------")

# def compare(score):
#     return score["math"]

#lambda score: score["math"]

scores.sort(key=lambda score:score["english"],reverse=False)
for score in scores:
    for value in score.values():
        print(f"{value:8} ", end="")
    print()
