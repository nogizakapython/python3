# 新規作成 2023/4/6
# じゃんけんゲーム、乱数を使って手をランダムに表示する

# 初期処理関数
def initial():
    print('じゃんけんをはじめます')
    player_name = input('名前を入力してください：')
    return player_name

# 入力値チェック関数
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

# じゃんけんの手選択処理
def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

# じゃんけんの結果判定関数
def judge(player, computer):
    if player == computer:
        return '引き分け'
    elif player == 0 and computer == 1:
        return '勝ち'
    elif player == 1 and computer == 2:
        return '勝ち'
    elif player == 2 and computer == 0:
        return '勝ち'
    else:
        return '負け'

# どちらか4勝した方を最終的な勝利にするためのメッセージ出力関数(最終結果関数)
def finish_judge(playername,player_win,computer_win,draw_count):
    if computer_win == 4:
        return (f"{player_win}勝{draw_count}分{computer_win}敗でコンピューターの勝ちです")
    else:
        return (f"{player_win}勝{draw_count}分{computer_win}敗で{playername}の勝ちです")        