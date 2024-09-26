array1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
leng1 = len(array1)

b_num = 0
e_num = 0
c_num = 0

def return_num(str1):
    for i in range(leng1):
        t1 = array1[i]
        if t1 == str1:
            r_num = i
    return r_num

X = input()
b_num = return_num(X)

Y = input()
e_num = return_num(Y)

C = input()
c_num = return_num(C)

if c_num >= b_num and c_num <= e_num:
    print("true")
else:
    print("false")
