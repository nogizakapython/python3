# じゃんけんゲーム
# 新規作成 2023/3/22

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# 関数 judge を定義してください
def judge(player,computer):
    # player と computer の比較結果によって条件を分岐してください
    if player == computer:
      return "引き分け"
    elif player == 0 and computer == 1:
      return "勝ち"
    elif player == 1 and computer == 2:
      return "勝ち"
    elif player == 2 and computer == 0:
      return "勝ち"
    else:
      return "負け"
      
    

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

if validate(player_hand):
    computer_hand = 1
   
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
    
    print_hand(computer_hand, 'コンピューター')
    
    # 変数 result に関数 judge の戻り値を代入してください
    result = judge(player_hand,computer_hand)
    # 変数 result を出力してください
    print("結果は" + result + "でした") 
else:    
    print('正しい数値を入力してください')