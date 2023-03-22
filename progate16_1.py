# じゃんけんゲームメインプログラム
# 新規作成 2023/3/22

# utils.py をモジュールとして読み込んでください
import progate16_2

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# utils モジュール内の関数 validate を呼び出してください
if progate16_2.validate(player_hand):
    computer_hand = 1

    if player_name == '':
        # utils モジュール内の関数 print_hand を呼び出してください
        progate16_2.print_hand(player_hand)
    else:
        # utils モジュール内の関数 print_hand を呼び出してください
        progate16_2.print_hand(player_hand, player_name)

    # utils モジュール内の関数 print_hand を呼び出してください
    progate16_2.print_hand(computer_hand, 'コンピュータ')
    
    # utils モジュール内の関数 judge を呼び出してください
    result = progate16_2.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
