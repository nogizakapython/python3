import re

s = input()
print(re.search(r'\d+(?=[KMGT]B)', s).start())
print(re.search(r'\d+(?=[KMGT]B)', s).group())