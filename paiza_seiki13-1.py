import re

s = input()
print(re.search(r'\$[0-9]{3,5}', s).start())