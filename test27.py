import json

data = {
         "秋元真夏": 30,
         "西野七瀬": 29
        }

# print(len(data))
# インテント付きJSONに変換
print(data)
for str1 in data:
    print(str1)
    print(data[str1])

data_str = json.dumps(data,indent=4,ensure_ascii=False)

# JSONをDictionaryに変換
data_obj = json.loads(data_str)

print(data_str)
# print(data_obj)
