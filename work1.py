# 文字と数値入力プログラム
# 新規作成 2023/2/28
#名前入力表示
print("Input your name ",end="")
# 入力した文字列を変数に渡す
name = input()
#数値入力表示
print("Input your number ",end="")
#入力した数値を変数に渡す
num = int(input())

#出力
print("はじめまして、%sさん" %name)
print("数値は%iです" %num)
