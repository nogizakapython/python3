# work21.py
# 新規作成 2023/3/15
# データを10件入力し、配列に格納して、集計結果を辞書配列に格納する

count = 0
limit = 10
array1 = []
result = {}
# 文字入力
while count < limit:
    str = input("文字を入力してください")
    array1.append(str)
    count += 1
#結果を集計する
for str in array1:
    if str not in result:
        result[str] = 0
    result[str] += 1

# print(result)
# 結果をfor文で取り出す
for key,value in result.items():
    print(f"{key}の値は{value}です")        
 