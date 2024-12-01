import re
str1 = input()
print(re.search(r'Math[123][ABC]',str1).start())

