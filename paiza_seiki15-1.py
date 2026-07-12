import re

s = input()
print(re.search(r'[^ ]*\.(jpg|png)', s).start())