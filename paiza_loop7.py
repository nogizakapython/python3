array1 = [8,16,24,32,40,48,56,64,72]
leng = len(array1)
str1 = ""
for i in range(0,leng):
    if i == 8:
        str1 = str1 + str(array1[i])
    else:
        str1 = str1 + str(array1[i]) + " "

print(str1)
