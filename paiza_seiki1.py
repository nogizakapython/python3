import re

str1 = input()
result1 = re.search("paiza",str1)
ans1 = str(result1)
array1 = ans1.split(',')
msg1 = array1[0]
ans = msg1.replace("<re.Match object; span=(","")
print(ans)
