# 新規作成 2023/3/15
# 集計結果を連想配列に格納する

member_s = ["men", "women", "men", "men", "women", "men","women"]
# stats = {"pass":4,"fall":2}

result = {}

for member in member_s:
    # 辞書にデータがない場合は0を入れる
    if member not in result:
        result[member] = 0
    result[member] += 1
    
print(result)    
    