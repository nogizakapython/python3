import re

str1 = input()
result1 = re.search('Math[123][ABC]',str1).start()
print(result1)
