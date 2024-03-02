import json

data = {
    "name": "秋元真夏",
    "age": 30
}

# インテント付きJSONに変換
data_str = json.dumps(data, indent=4, ensure_ascii=False)
# JSONをDictionaryに変換
data_obj = json.loads(data_str)

print(data_str)
print(data_obj)
