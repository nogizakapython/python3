num = int(input())
array1 = []
for i in range(num):
    array1.append(input())

target_age = int(input())   
for data1 in array1:
    n,a,b,s = map(str,data1.split(" "))
    a = int(a)
    if a == target_age:
        print(n)