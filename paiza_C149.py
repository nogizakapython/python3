str1 = input()
str2 = input()
array1 = list(str1)
array2 = list(str2)
num1 = len(array1)
num2 = len(array2)
ans = ""
for i in range(num2):
    char1 = array2[i]
    char2 = char1.upper()
    char3 = char1.lower()

    for j in range(num1):
        target_char = array1[j]
        if char2 == target_char:
            ans = ans + char2
        elif char3 == target_char:
            ans = ans + char3

print(ans)
