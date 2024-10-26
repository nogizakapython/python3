import re

str1 = input()

match1 = "paiza"

result1 = re.search(match1,str1)
if result1:
  print("OK")
else:
  print("NG")
