# 新規作成 2023/3/13
# 辞書のソート処理

scores = [
  {"name": "秋元真夏", "math": 77, "english": 92},
  {"name": "中田花奈", "math": 85, "english": 84},
  {"name": "賀喜遥香", "math": 82, "english": 75},
  {"name": "早川聖来", "math": 73, "english": 76},
]

print("Name      Math           English")
print("--------- -------------- --------------")

def compare(score):
    return score["math"]

#lambda score: score["math"]

scores.sort(key=compare,reverse=True)
for score in scores:
    for value in score.values():
        print(f"{value:10} ", end="")
    print()
