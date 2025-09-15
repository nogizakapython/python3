str1,str2 = map(str,input().split(' '))
leng1 = len(str1)
str1_last = str1[leng1-1]
str2_first = str2[0]
if str1_last == str2_first:
    print("YES")
else:
    print("NO")
