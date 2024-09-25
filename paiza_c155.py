import re

str1 = input()
n = int(input())
for i in range(n):
    target_word = input()
    flag1 = re.search(str1,target_word)
    if flag1:
        print("Yes")
    else:
        print("No")
