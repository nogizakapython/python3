n = int(input())
array1 = []
array2 = []
array3 = []
for i in range(n):
    A,B = input().split(' ')
    array1.append(A + "," + B)
    array2.append(A)

for str1 in array2:
    count = 0
    for ch in array1:
        array4 = ch.split(',')
        C = array4[0]
        D = int(array4[1])
        if C == str1:
            count += D
    array3.append(str(count) + "," + str1)

array5 = list(set(array3))
array6 = {}
for str2 in array5:
    w_array = str2.split(',')
    value = int(w_array[0])
    key = w_array[1]
    array6[key] = value

array7 = sorted(array6.items(), key=lambda x:x[1])
array8 = []
leng1 = len(array7)
for i in range(leng1-1,-1,-1):
    str10 = array7[i]
    str11 = str(str10)
    w_array2 = str11.split(',')
    key1 = w_array2[0]
    key1 = key1.replace("(","")
    key1 = key1.replace("'",'')

    value1 = w_array2[1]
    value1 = value1.replace(')',"")
    print(key1 + value1)
