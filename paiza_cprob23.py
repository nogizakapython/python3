N,C = map(int,input().split(" "))
P = int(input())
array1 = list(map(int,input().split(" ")))
array2 = []
for i in array1:
    if i % N == 0:
        array2.append(i)
#print(array2)
flag = 0
for j in range(C):
    d = int(input())
    flag = 0
    for k in range(len(array2)-1):
        target1 = array2[k]
        target2 = array2[k+1]
        #print(d)
        if d < target1 and flag == 0:
            print(target1)
            flag += 1    
        elif d >= target1 and d <= target2 and flag == 0 :
            if abs(d - target1) < abs(d-target2):
                print(target1)
                flag += 1
                
            else:
                print(target2)
                flag += 1
        elif k == len(array2)-2 and flag == 0:
            print(target2)
            flag += 1