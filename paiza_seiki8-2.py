import re


def search_num(search_word,s):
  return(re.search(search_word,s).start())

def main():
  s = input()
  word = r'congratulations!*'
  ans = search_num(word,s)
  print(ans)


if __name__ == "__main__":
  main()
