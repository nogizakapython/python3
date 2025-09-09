import re

s = input()
print(re.search(r'[A-Z]-[0-9][0-9][ab]', s).start())
