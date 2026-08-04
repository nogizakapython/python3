import re

s = input()
print(re.search(r'\w{3}-\d{3,4}', s).start())