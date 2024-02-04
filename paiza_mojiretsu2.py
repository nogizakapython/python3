input_line = input()
array1 = []
for i in input_line:
    if i not in array1:
        array1.append(i)
        print(i,end="")

