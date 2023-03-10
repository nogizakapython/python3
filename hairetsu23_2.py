# 新規作成 2023/3/10
# 辞書のソート処理

scores = [
  {"name": "Taro", "math": 70, "english": 82},
  {"name": "Jiro", "math": 67, "english": 61},
  {"name": "Saburo", "math": 81, "english": 58},
  {"name": "Siro", "math": 47, "english": 70},
]

print("Name     Math     English")
print("-------- -------- --------")

def compare(score):
    return score["math"]

#lambda score: score["math"]

scores.sort(key=compare,reverse=True)
for score in scores:
    for value in score.values():
        print(f"{value:8} ", end="")
    print()
