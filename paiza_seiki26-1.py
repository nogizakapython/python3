import re

s = input()
print(re.search(r'\{.*?\}', s).start())
print(re.search(r'\{.*?\}', s).group())