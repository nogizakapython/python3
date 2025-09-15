import re

s = input()
print(re.search(r'ID-[0-9]+', s).start())
