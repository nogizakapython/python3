# 小樽商科大2010年の入試問題
# 2010!は2で何回割り切れるか


def two_div(num):
  two_div_count = 0
  while num % 2 == 0:
    two_div_count += 1
    num /= 2
  return two_div_count

def main():
  N = 2010
  two_div_ans = sum(map(two_div,range(1,N+1)))
  print(two_div_ans)

if __name__ == "__main__":
  main()
