# じゃんけんゲーム
# 新規作成 2023/3/8


import random
 
def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')
    
def d_hand(num):
  match(num):
    case 0:
      hand1 = "グー"
      return hand1
    case 1:
      hand1 = "チョキ"
      return hand1
    case 2:
      hand1 = "パー"
      return hand1 
    
      
print('じゃんけんをはじめます')
m_hand = ""
c_hand = ""
# input を用いて入力を受け取り、変数 player_name に代入してください
player_name = input("名前を入力してください：")
# じゃんけんの手を入力する
while True:
  try:
    w_hand = input("じゃんけんの手「グー」または「チョキ」または「パー」を入力する：")
    if w_hand != "グー" and w_hand != "チョキ" and w_hand != "パー":
      raise ValueError
    m_hand = w_hand
    break
  except:
    print("グー、チョキ、パーのどれかの手を入力してください")
# 変数 player_name の値によって関数 print_hand の呼び出し方を変更してください
w_num = random.randint(0,2)
        
c_hand = d_hand(w_num)

if player_name == "":
  player_name = "ゲスト"

if m_hand == c_hand:
  print("あいこです")
elif m_hand == "グー" and c_hand == "パー":
  print(f"{player_name}の負けです")
elif m_hand == "グー" and c_hand == "チョキ":
  print(f"{player_name}の勝ちです")
elif m_hand == "チョキ" and c_hand == "グー":
  print(f"{player_name}の負けです")
elif m_hand == "チョキ" and c_hand == "パー":
  print(f"{player_name}の勝ちです")
elif m_hand == "パー" and c_hand == "チョキ":
  print(f"{player_name}の負けです")
elif m_hand == "パー" and c_hand == "グー":
  print(f"{player_name}の勝ちです")
          