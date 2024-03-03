import re

str1 = "<p>・F-Gene（B型事業所）</p>"

result1 = re.search('<p>',str1)
if result1:
  print("OK")
