# 北見工業大2024年の入試問題
# 2の2024乗を7で割った余りを求める


def seven_div_remainder(num):
  remainder = 0
  remainder = num % 7
  return remainder


def main():
  base_number = 2
  power_number = 2024
  for i in range(0,power_number+1):
    num = pow(2,i)
    ans = seven_div_remainder(num)
  print(ans)


if __name__ == "__main__":
  main()
