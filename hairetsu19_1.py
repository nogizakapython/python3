# 集合
# 和集合、積集合、差集合
# 新規作成 2023/3/9

eng_members = ["Taro", "Jiro", "Saburo"]
math_members = ["Jiro", "Saburo", "Shiro"]

# set関数で配列を集合に変換する
eng_members = set(eng_members)
math_members = set(math_members)

#和集合を表示する
print(eng_members | math_members)

#積集合を表示する
print(eng_members & math_members)

# 差集合
print(eng_members - math_members)
print(math_members - eng_members)
