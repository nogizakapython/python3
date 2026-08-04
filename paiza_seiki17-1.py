import re

s = input()
print('Yes' if re.search(r'^Re:', s) else 'No')