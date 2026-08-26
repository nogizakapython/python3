import re

s = input()
print(re.sub(r'/\*.*\*/', r'', s, 1))
