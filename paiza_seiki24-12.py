import re

s = input()
array1 = re.split(r'-{3,}',s)
for i in array1:
    print(i)