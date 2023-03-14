def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    # 変数 computer_hand に数値 1 を代入してください
    computer_hand = 1


    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)

    # 第1引数を computer_hand 、第2引数を文字列「 コンピューター 」として関数 print_hand を呼び出してください
    print_hand(computer_hand,"コンピューター")

else:
    print('正しい数値を入力してください')
