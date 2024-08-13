A,B,C = map(int,input().split(" "))
array1 = input().split(' ')
array1.sort()
count = 0
if B * C > A :
    count = A 
else:
    count = B * C
for j in range(B*(C-1),count):
        print(array1[j])
