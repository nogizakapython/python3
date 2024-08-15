n = int(input())
array1 = []
for i in range(n):
    data = input()
    if data in array1:
        m = len(array1)
        for j in range(m):
            w_data = array1[j]
            if w_data == data:
                array1.pop(j)
                array1.insert(0,w_data)
    else:
        array1.insert(0,data)

for k in array1:
    print(k)