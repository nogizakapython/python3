# ディクショナリー配列(連想配列)
# 新規作成 2023/3/7

scores = {"math":62,"english":91,"physics":84}
print(scores)
scores["math"] = 71
print(scores["english"])
print(scores["math"])

scores["biology"] = 50
print(scores)

popped_value = scores.pop("english")
scores["english"] = 55
del scores["english"]

print(scores)
print(popped_value)
