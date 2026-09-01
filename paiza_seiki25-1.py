import re

s = input()
print(re.search(r'G[A-Z]??C', s).start())
print(re.search(r'G[A-Z]??C', s).group())