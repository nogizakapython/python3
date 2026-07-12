import re

s = input()
print(re.search(r'(%[0-9A-Za-z]{2}){2,}', s).start())