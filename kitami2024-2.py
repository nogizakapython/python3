# 北見工業大2024年の入試問題
# 2の2024乗を7で割った余りを求める

seven_remainder_array = []

def seven_div_remainder(num):
  remainder = num % 7
  return remainder


def main():
  base_number = 2
  power_number = 2024

  for i in range(0,power_number+1):
      num = pow(base_number,i)
      ans = seven_div_remainder(num)
      seven_remainder_array.append(ans)

  print(seven_remainder_array[len(seven_remainder_array)-1])

if __name__ == "__main__":
  main()
