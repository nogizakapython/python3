# 新規作成 2023/3/31
# jupyter notebookでのソース

# 配列定義
cities = ['東京','パリ','ロンドン','北京']
r_num = 0
while True:
    try:
        num = int(input("数字を入力してください"))
        if num < 0 or num > len(cities):
            raise ValueError
        else:
            r_num = num
            break
    except:
        print(f"0以上{len(cities)}までの数字を入力してください")


print(cities[r_num])
