input_line = input()
array1 = input_line.split(' ')
X = int(array1[0])
Y = int(array1[1])
Z = int(array1[2])
if X >= 10 and Y >= 10:
    print("YES")
elif Z >= 10:
    print("YES")
else:
    print("NO")
