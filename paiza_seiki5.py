import re

str1 = input()
result = re.search('[^1234567890]',str1).start()
print(result)
