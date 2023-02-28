# 数値当て
# 新規作成 2023/2/28
#randomライブラリを読み込む
import random
# 1～10までの整数をランダムに表示する
answer = random.randint(1,10)
# 数値の入力を促す
print("Your guess? ",end="")
# 入力した数値を変数に受け取る
guess = int(input())

# 正解の場合は「Bingo」間違っている場合は「Boo....」で表示
if answer == guess:
    print("Bingo")
elif answer > guess:
    print("Bigger!")
elif answer < guess:
    print("Smaller!")    

#答えを表示
print("[Answer:%i]" %answer)   