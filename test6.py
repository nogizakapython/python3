# 数値当て
# 新規作成 2023/2/28
answer = 6
# 数値の入力を促す
print("Your guess? ",end="")
# 入力した数値を変数に受け取る
guess = int(input())

# 正解の場合は「Bingo」間違っている場合は「Boo....」で表示
if answer == guess:
    print("Bingo")
else:
    print("Boo....")
            