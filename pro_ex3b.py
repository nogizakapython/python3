#　辞書のキーから値を取り出すプログラム
#  新規作成 2023/4/5
#  修正    2023/4/6 (要素の番号ではなく要素のキーを入力する方法に変更) 
#  修正    2023/4/7  入力チェックで配列の要素を指定

menus={"pork":"豚肉","beaf":"牛肉","chicken":"鶏肉","fish":"魚肉"}

str = ""

while True:
    item = input(f"{','.join(menus)}の中から1つ単語を選んでください ")
    if item in menus:
        print(menus[item])
        break
    else:
        print("入力した単語が間違っています")
                



    
    