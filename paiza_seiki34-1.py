import re

s = input()
print(re.search(r'(?<=Date: )[0-9/]+', s).start())
print(re.search(r'(?<=Date: )[0-9/]+', s).group())