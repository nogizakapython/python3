
# 再帰関数
def test(n):

  if n > 0:
     test(n - 1)
  

  print(n)


# メイン関数
def main():
    test(3)


if __name__ == "__main__":
   main()    