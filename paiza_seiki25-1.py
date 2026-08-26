import re

s = input()
print(re.sub(r'import [a-zA-Z0-9]+', r'', s))
