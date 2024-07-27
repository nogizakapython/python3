array1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num1 = int(input())
data1 = input()
array2 = list(data1)
c_num = len(array1)
for j in range(c_num):
    str1 = array1[j]
    count = 0
    for i in range(num1):
        str2 = array2[i]
        if str1 == str2:
            count += 1

    if j == c_num - 1:
        print(count,end="")
    else:
        print(count,end=" ")
