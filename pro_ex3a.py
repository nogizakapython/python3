#　辞書のキーから値を取り出すプログラム
#  新規作成 2023/4/5
#  修正    2023/4/6 (要素の番号ではなく要素のキーを入力する方法に変更) 

menus={"pork":"豚肉","beaf":"牛肉","chicken":"鶏肉","fish":"魚肉"}

str = ""

while True:
    try:
        str1 = input(f"pork,beaf,chicken,fishの4つから1つの単語を選んでください ")
        if str1 != "pork" and str1 != "beaf" and str1 != "chicken" and str1 != "fish":
            raise ValueError
        else:
            str = str1
            break
    except:
        print("入力文字が間違っています")    


# print(list(menus.items())[number])
# 
print(f"{menus[str]}")

    
    