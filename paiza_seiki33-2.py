import re

s = input()
msg = r'Java(?!Script)'
print(re.search(msg, s).start())
print(re.search(msg, s).group())