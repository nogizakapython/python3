import re

s = input()
print(re.search(r'Java(?!Script)', s).start())
print(re.search(r'Java(?!Script)', s).group())