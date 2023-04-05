# 新規作成 2023/4/5
#　辞書の要素の

menus={"pork":"豚肉","beaf":"牛肉","chicken":"鶏肉"}

number = 0

while True:
    try:
        input_num = int(input(f"番号を0から{len(menus)}の間で入力してください "))
        if input_num < 0 or input_num >= len(menus):
            raise ValueError
        else:
            number = input_num
            break
    except:
        print("数字の入力が間違っています")    


# print(list(menus.items())[number])
# 
key,value = list(menus.items())[number]
print(f"{key}の意味は{value}です")

    
    