import re

s = input()
print(re.search(r'(?:n|st|vac)ation([0-9a-zA-Z]+)', s).group(0))
print(re.search(r'(?:n|st|vac)ation([0-9a-zA-Z]+)', s).group(1))
