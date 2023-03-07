# 連想配列の要素の取り出し
# 新規作成 2023/3/8

scores = {"math": 62, "english": 91, "physics": 84}

# for key in scores.keys():
#     print(key)

# for value in scores.values():
#     print(value)

for item in scores.items():
    key,value = item
    print(f"{key:8} {value:3}")


scores2 = {"biology": 70, "history": 54, "kobun": 90}

for key,value in scores2.items():
    print(f"{key:8} {value:3}")
