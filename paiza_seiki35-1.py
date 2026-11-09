import re

s = input()
print(re.search(r'(?<!\[Feature\] )[A-Z][^\[\]]*?\.', s).start())
print(re.search(r'(?<!\[Feature\] )[A-Z][^\[\]]*?\.', s).group())