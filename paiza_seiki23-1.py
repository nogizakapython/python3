import re

s = input()
print(re.sub(r'raw_input', r'input', s))