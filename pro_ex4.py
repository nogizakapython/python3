# 新規作成 2023/4/5
# 辞書から要素を取り出して表示する

# 文字列のキーと数値の値を持つ辞書を作って、変数 items に代入してください
items = {'pork':150,'chicken':300,'beaf':200}

# output関数
def output1():
    print('---------------------------------------------')



# for 文を用いて、辞書 items のキーを1つずつ取り出していく繰り返し処理を作成してください
for item_name in items:
    # 「 --------------------------------------------- 」を出力してください
    output1()
    # 「 ◯◯は1個△△円です 」となるように出力してください
    print(item_name + "は1個" + str(items[item_name]) + "円です")
    if item_name == "beaf":
        output1()