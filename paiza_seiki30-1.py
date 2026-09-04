import re

s = input()
print(re.search(r'\|.{3,10}?\|', s).start())
print(re.search(r'\|.{3,10}?\|', s).group())
