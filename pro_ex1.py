# 新規作成 2023/4/5
#　配列の表示

menus=["いろはす","富士山の銘水","桃の天然水","炭酸水"]

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


print(menus[number])

    
    