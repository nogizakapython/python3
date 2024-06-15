import re
str1 = input()
array1 = list(map(int,re.split('[+-]',str1)))
# print(array1)
len1 = len(str1)
p = 0
ans = 0
calc1 = ""
for i in range(len1):
    str2 = str1[i]
    if i == len1-1:
      number1 = array1[p]
      if calc1 == "+":
        ans += number1
      elif calc1 == "-":
        ans -= number1
    if str2 == "+" or str2 == "-":
        number1 = array1[p]
        if p == 0:
            ans += number1
        elif p > 0:
            if calc1 == "+":
                ans += number1
            else:
                ans -= number1
        if str2 == "+":
            calc1 = str2
        else:
            calc1 = str2
        p += 1

print(ans)
