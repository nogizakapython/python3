array1 = []
for i in range(5):
    data1 = input()
    array2 = list(data1)
    array1.append(array2)
#print(array1)
cross1 = ""
cross2 = ""
O_count = 0
X_count = 0
for j in range(0,5):
    str1 = array1[j][j]
    cross1 += str1
    str2 = array1[j][4-j]
    cross2 += str2

if cross1 == "OOOOO":
    O_count += 1
elif cross1 == "XXXXX":
    X_count += 1

if cross2 == "OOOOO":
    O_count += 1
elif cross2 == "XXXXX":
    X_count += 1

if O_count > X_count:
    print("O")
elif O_count < X_count:
    print("X")
else:
    print("D")
