import re

n = int(input())
array1 = []
for _ in range(n):
    data = input()
    array1.append(data)

s_word = input()
for d in array1:
    num1 = re.search(s_word,d)
    if num1 != None:
      ans = d.split(' ')
      print(ans[0])
