import re

s = input()
print(re.search(r'accept|reject|pending', s).start())