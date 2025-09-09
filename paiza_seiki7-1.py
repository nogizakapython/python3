import re

s = input()
print(re.search(r'clang-?format', s).start())
