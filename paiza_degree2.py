#################################
####  並び替え処理
#################################

# 入力データリストの定義
jumper_data = []

# 縄跳びに参加する人数を入力、及び入力データのチェック関数
def input_jumper_count():
  print("人数を0より大きい整数で入力してください")
  while True:
    try:
      num = int(input())
      if num > 0:
        return num
      else:
        print("0より大きい整数を入力してください")
    except TypeError:
        print("0より大きい整数以外、入力しないでください")

#１分間に縄跳びを飛んだ回数を入力する関数
def input_jump_data(data_count):
  for i in range(data_count):
    print("1分間の縄跳びの回数を0以上の整数で入力してください")
    while True:
      try:
        jump_times = int(input())
        if jump_times >= 0:
          break
        else:
          print("0以上の整数を入力してください。")
      except TypeError:
        print("0以上の整数以外、入力しないでください")
    jumper_data.append(jump_times)


def main():
  num = input_jumper_count()
  input_jump_data(num)
  #回数データを降順に並び替え,ランキングリストに格納する
  ranking = sorted(jumper_data,reverse=True)
  # 順位を決定し、標準出力に出力する。
  for degree,data in enumerate(jumper_data,1):
    rank = ranking.index(data) + 1
    print(f"{degree}番目の人の順位は{rank}位です")


if __name__ == "__main__":
  main()
