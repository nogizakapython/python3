import re

s = input()
print(re.search(r'[0-9a-f]{64}', s).start())
print(re.search(r'[0-9a-f]{64}', s).group())