# 新規作成 2023/3/22
# じゃんけんゲームのメインモジュール

# 関数モジュールの読み込み
import progate17_2
# random モジュールを読み込む
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if progate17_2.validate(player_hand):
    # randint を用いて 0 から 2 までの数値を取得し、変数 computer_hand に代入してください
    computer_hand = random.randint(0,2) 
    
    if player_name == '':
        progate17_2.print_hand(player_hand)
    else:
        progate17_2.print_hand(player_hand, player_name)

    progate17_2.print_hand(computer_hand, 'コンピューター')
    
    result = progate17_2.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
