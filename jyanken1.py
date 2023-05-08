# 新規作成 2023/4/6
# じゃんけんゲームのメインモジュール
# 勝ち抜きゲームでプレイヤーかコンピュータのどちらかが4勝した方の勝利
# 最終的なじゃんけんの結果を出力する

# 関数モジュールの読み込み
import jyanken2
# random モジュールを読み込む
from random import randint
# コンピュータ勝利数
computer_win = 0
# プレイヤー勝利数
player_win = 0
# 引き分け数
draw_count = 0
# 勝利数設定
win_count = 4
playername = ""

# 初期処理(名前の登録)
playername = jyanken2.initial()
if playername == "":
    playername = "ゲスト"

# メイン処理
while True:
        
    print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
    player_hand = int(input('数字で入力してください：'))
    # 入力値チェック
    if jyanken2.validate(player_hand):
        # randint を用いて 0 から 2 までの数値を取得し、変数 computer_hand に代入してください
        computer_hand = randint(0,2) 
    
        if playername == '':
            jyanken2.print_hand(player_hand)
        else:
            jyanken2.print_hand(player_hand, playername)

        jyanken2.print_hand(computer_hand, 'コンピューター')
    
        result = jyanken2.judge(player_hand, computer_hand)
        print('結果は' + result + 'でした')
        if result == "勝ち":
            player_win += 1
        elif result == "負け":
            computer_win += 1
        else:
            draw_count += 1    
        
        if computer_win == win_count or player_win == win_count:
            break    
                
    else:
        print('正しい数値を入力してください')

# 最終的なじゃんけん勝ち抜き戦の結果を出力する
f_result = jyanken2.finish_judge(playername,player_win,computer_win,draw_count)
print(f_result)
