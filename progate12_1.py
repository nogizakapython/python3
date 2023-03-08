# じゃんけんゲームひな形
# 新規作成 2023/3/8
 
def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

# input を用いて入力を受け取り、変数 player_name に代入してください
player_name = input("名前を入力してください：")

# 変数 player_name の値によって関数 print_hand の呼び出し方を変更してください
if player_name == "":
  print_hand('グー')
else:
  print_hand('グー',player_name)