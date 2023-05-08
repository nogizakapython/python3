scores = [
  {"name": "秋元真夏", "math": 77, "english": 85},
  {"name": "橋本奈々未", "math": 80, "english": 78},
  {"name": "松村沙友理", "math": 85, "english": 66},
  {"name": "池田瑛紗", "math": 75, "english": 88},
  {"name": "北川悠理", "math": 76, "english": 96},
]

print("Name       Math       English")
print("---------- ---------- ----------")

# def compare(score):
#     return score["math"]

#lambda score: score["math"]    
    
scores.sort(key=lambda score:score["english"],reverse=True)
for score in scores:
    for value in score.values():
        print(f"{value:8} ", end="")
    print()