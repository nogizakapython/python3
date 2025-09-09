import re

s = input()
print(re.search(r'congratulations!*', s).start())
