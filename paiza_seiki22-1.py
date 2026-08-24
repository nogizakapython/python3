import re

s = input()
print(re.sub(r'(\d{2})\.(\d{2})', r'\1/\2', s, 1))