#################################
####  並び替え処理
#################################

def errormsg1():
  print("0より大きい整数を入力してください")

def setValue(num):
    flag1 = 0
    if num > 0:
      return flag1
    else:
      flag1 += 1
      return flag1


def main():
  print("データ数を0より大きい整数で入力してください")
  while True:
    try:
      num = int(input())
      result1 = setValue(num)
      if result1 == 0:
        break
      else:
        raise ValueError
    except TypeError:
      errormsg1()
    except ValueError:
      errormsg1()

  array1 = []
  for i in range(num):
    print("1分間の縄跳びの回数を0より大きい整数で入力してください")
    while True:
      try:
        data = int(input())
        result2 = setValue(data)
        if result2 == 0:
          break
        else:
          raise ValueError
      except TypeError:
        errormsg1()
      except ValueError:
        errormsg1()

    array1.append(data)

  #回数データを降順に並び替える
  array2 = sorted(array1,reverse=True)
  array3 = []
  degree = 0
  before_value = 0
  count = 1
  # 順位配列を作成する
  for j in list(array2):
    if not j == before_value:
        degree += count
        count = 1
    else:
        count += 1
    array3.append(degree)
    before_value = j

  # 順位を表示する
  count2 = 1
  for k in list(array1):
      elem = array2.index(k)
      print(f"{count2}番目に入力したデータは{array3[elem]}位です")
      count2 += 1
if __name__ == "__main__":
  main()
