n = int(input())
array1 = []
array2 = []
for i in range(n):
    array1.append(input())
for j in range(n):
    data1 = array1[j]
    name,age,birth,state = data1.split(' ')
    array2.append(age + " " + name + " " + birth + " " + state)
    
array2.sort()    
for k in range(n):
    data2 = array2[k]
    age,name,birth,state = data2.split(' ')
    print(name + " " + age + " " + birth + " " + state)