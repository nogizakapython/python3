# 文字列入力関数
def input_str():
  str1 = input()
  return str1

def make_array(str1):
  import re
  array1 = list(map(int,re.split('[+-]',str1)))
  return array1
# 足し算関数
def add(ans,num):
  ans += num
  return ans
# 引き算関数
def gain(ans,num):
  ans -= num
  return ans

def main():
  # 文字列の入力
  str1 = input_str()
  # 入力した文字を配列に分割する
  array1 = make_array(str1)
  # 配列の長さ
  len1 = len(str1)
  # 配列の要素変数
  p = 0
  # 回答変数
  ans = 0
  # 演算記号変数
  calc1 = ""
  for i in range(len1):
      str2 = str1[i]
      if i == len1-1:
        number1 = array1[p]
        if calc1 == "+":
          ans = add(ans,number1)
        elif calc1 == "-":
          ans = gain(ans,number1)
      if str2 == "+" or str2 == "-":
        number1 = array1[p]
        if p == 0:
            ans = add(ans,number1)
        elif p > 0:
            if calc1 == "+":
                ans = add(ans,number1)
            else:
                ans = gain(ans,number1)
        if str2 == "+":
            calc1 = str2
        else:
            calc1 = str2
        p += 1

  print(ans)


if __name__ == "__main__":
  main()
