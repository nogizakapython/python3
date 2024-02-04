input_line = input()
array1 = set()
for i in input_line:
    if i not in array1:
        array1.add(i)
        print(i,end="")

