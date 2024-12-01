import re

s = input()
print(re.search(r'[^0123456789].....', s).start())
