num = int(input())
array1 = []
for i in range(num):
    data = input()
    if data == "out":
        if len(array1) > 0:
            array1.pop(0)
    else:
        w_array = data.split(' ')
        i_data = int(w_array[1])
        array1.append(i_data)


for number in array1:
    print(number)
