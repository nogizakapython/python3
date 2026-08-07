import re

s = input()
for i in re.findall(r'[^ ]+@[^ ]+', s):
    print(i)