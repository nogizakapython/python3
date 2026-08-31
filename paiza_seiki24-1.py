import re

s = input()
for i in re.split(r'-{3,}', s):
    print(i)